# -*- coding: UTF-8 -*-

import  logging
import traceback

import pymysql
from myapp.engines.models import ResultsSet
from . import EngineBase

logger = logging.getLogger('default')

class MySQLEngine(EngineBase):

    def get_connection(self, db_name=None):
        if self.conn:
            return self.conn
        if db_name:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port=int(self.port),
                                        database=self.database,charset=self.instance.charset or 'utf8mb4')
        else:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port = int(self.port),
                                        charset=self.instance.charset or 'utf8mb4')
        return self.conn

    def query_set(self, db_name=None, sql='', limit_num=0, close_conn=True):

        # 实例化ResultSet类

        results_set = ResultsSet(full_sql=sql)
        # return results_set
        # return 3

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

    def query_check(sql=''):
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

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None