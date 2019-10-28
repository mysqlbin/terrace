# -*- coding: UTF-8 -*-

import  logging
import traceback
import sqlparse
import re
import pymysql
from myapp.engines.models import ResultsSet
from . import EngineBase

logger = logging.getLogger('default')

class MySQLEngine(EngineBase):   # 类继承

    def get_connection(self, db_name=None):
        if self.conn:
            return self.conn
        if db_name:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port=int(self.port),
                                        database=db_name,charset=self.instance.charset or 'utf8mb4')
        else:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port = int(self.port),
                                        charset=self.instance.charset or 'utf8mb4')
        return self.conn

    @property
    def server_version(self):
        version = self.query_set(sql="select @@version").rows[0][0][0:3]
        version = version.replace('.', '')
        return int(version)

    def query_set(self, db_name=None, sql='', limit_num=0, close_conn=True):

        # 实例化ResultSet类
        results_set = ResultsSet(full_sql=sql)
        try:
            conn = self.get_connection(db_name=db_name)
            cursor = conn.cursor()
            effect_row = cursor.execute(sql)
            results_set.effect_row = effect_row
            colnames = [desc[0] for desc in cursor.description]
            results_set.column_list = colnames
            if int(limit_num) > 0:
                rows = cursor.fetchmany(size=limit_num)
            else:
                rows = cursor.fetchall()
            results_set.rows = rows

        except Exception as e:
            logger.error(f"MySQL语句执行报错，语句：{sql}，错误信息{traceback.format_exc()}")
            results_set.error = str(e)

        finally:
            if close_conn:
                self.close()

        return results_set

    def query_check(self, sql=''):
        result = {'msg': '', 'bad_query': False, 'filtered_sql': sql, 'has_star': False}
        try:
            sql = sqlparse.format(sql, strip_comments=True)
            sql = sqlparse.split(sql)[0]
            result['filtered_sql'] = sql.strip()
        except Exception as err:
            result['bad_query'] = True
            result['msg'] = 'SQL语句无效'

        if re.match("select|show|explain|desc", sql) is None:
            result['bad_query'] = True
            result['msg'] = '不支持的语句类型'
        if re.search('\*', sql) is not None:
            result['has_star'] = True
            result['msg'] = 'SQL语句中含有 * '
        return result

    def get_variables(self, variables=None):
        """获取实例参数"""
        if variables:
            variables = "','".join(variables) if isinstance(variables, list) else "','".join(list(variables))
            db = 'performance_schema' if self.server_version >= int(57) else 'information_schema'
            sql = f"""select * from {db}.global_variables where variable_name in ('{variables}');"""
        else:
            sql = "show global variables;"

        return self.query_set(sql=sql)

    def get_status(self, status=None):
        """获取实例状态信息"""
        if status:
            db = 'performance_schema' if self.server_version >= int(57) else 'information_schema'
            if isinstance(status, list):
                status = "','".join(status)
                sql = f"""select * from {db}.global_status where variable_name in ('{status}');"""
            else:
                sql = f"""select * from {db}.global_status where variable_name = '{status}';"""
        else:
            sql = "show global status;"

        return self.query_set(sql=sql)

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None