#!/bin/env python
#-*-coding:utf-8-*-
import pymysql
import sys,string,time,datetime
import logging
import traceback
import sqlparse
import re
from myapp.common.utils.aes_decryptor import Prpcrypt

logger = logging.getLogger('default')

def mysql_query(sql,user,passwd,host,port,dbname):
    result = ''
    column_list = ''
    try:
        conn   = pymysql.connect(host=host,user=user,passwd=passwd,port=int(port),connect_timeout=5,charset='utf8mb4')
        conn.select_db(dbname)
        cursor = conn.cursor()
        cursor.execute(sql)
        fileds  = cursor.description
        column_list =[]
        #获取列名
        for i in fileds:
            column_list.append(i[0])
        result = cursor.fetchall()
        error = ''
    except Exception as e:
        logger.error(f"MySQL语句执行报错，语句：{sql}，错误信息{traceback.format_exc()}")
        error = str(e)
    finally:
        cursor.close()
        conn.close()

    return (result, column_list, error)

def get_process_data(insname,sql, dbname = 'information_schema'):
    flag = True
    pc = Prpcrypt()

    #多对多的查询
    #SELECT `myapp_db_name`.`id`, `myapp_db_name`.`dbtag`, `myapp_db_name`.`dbname` FROM `myapp_db_name` INNER JOIN `myapp_db_name_instance` ON (`myapp_db_name`.`id` = `myapp_db_name_instance`.`db_name_id`) WHERE `myapp_db_name_instance`.`db_instance_id` = 7; args=(7,)
    for a in insname.db_name_set.all():    #models.py：Db_name
        #SELECT `myapp_db_account`.`id`, `myapp_db_account`.`user`, `myapp_db_account`.`passwd`, `myapp_db_account`.`role`, `myapp_db_account`.`tags` FROM `myapp_db_account` INNER JOIN `myapp_db_account_dbname` ON (`myapp_db_account`.`id` = `myapp_db_account_dbname`.`db_account_id`) WHERE `myapp_db_account_dbname`.`db_name_id` = 2; args=(2,)
        for i in a.db_account_set.all():   #models.py：Db_account
            if i.role == 'admin':
                #获取账号和密码，用来连接数据库
                username = i.user
                passwd = pc.decrypt(i.passwd)
                # passwd = i.passwd
                flag = False
                break
        if flag == False:
            break
    if 'username' in vars():
        results, column_list, error = mysql_query(sql, username, passwd, insname.ip, int(insname.port), dbname)
        return results, column_list, error
    else:
        return (['PLEASE set the admin role account FIRST'], ''), ['error']



def mysql_query_set(sql,user,passwd,host,port,dbname,limit_num):

    result = {'effect_row': '', 'msg': 'ok', 'rows': '', 'column_list': ''}

    try:
        conn   = pymysql.connect(host=host,user=user,passwd=passwd,port=int(port),connect_timeout=5,charset='utf8mb4')
        conn.select_db(dbname)
        cursor = conn.cursor()
        effect_row = cursor.execute(sql)
        result['effect_row'] = effect_row
        colnames = [desc[0] for desc in cursor.description]
        result['column_list'] = colnames
        if int(limit_num) > 0:
            rows = [dict(zip(colnames, row)) for row in cursor.fetchmany(size=limit_num)]
        else:
            rows = [dict(zip(colnames, row)) for row in cursor.fetchall()]
        result['rows'] = rows
    except Exception as e:
        logger.error(f"MySQL语句执行报错，语句：{sql}，错误信息{traceback.format_exc()}")
        result['msg'] = str(e)
    finally:
        cursor.close()
        conn.close()

    return result

def get_process_data_set(insname,sql, dbname = 'information_schema', limit_num = 0):
    flag = True
    pc = Prpcrypt()

    #多对多的查询
    #SELECT `myapp_db_name`.`id`, `myapp_db_name`.`dbtag`, `myapp_db_name`.`dbname` FROM `myapp_db_name` INNER JOIN `myapp_db_name_instance` ON (`myapp_db_name`.`id` = `myapp_db_name_instance`.`db_name_id`) WHERE `myapp_db_name_instance`.`db_instance_id` = 7; args=(7,)
    for a in insname.db_name_set.all():    #models.py：Db_name
        #SELECT `myapp_db_account`.`id`, `myapp_db_account`.`user`, `myapp_db_account`.`passwd`, `myapp_db_account`.`role`, `myapp_db_account`.`tags` FROM `myapp_db_account` INNER JOIN `myapp_db_account_dbname` ON (`myapp_db_account`.`id` = `myapp_db_account_dbname`.`db_account_id`) WHERE `myapp_db_account_dbname`.`db_name_id` = 2; args=(2,)
        for i in a.db_account_set.all():   #models.py：Db_account
            if i.role == 'admin':
                #获取账号和密码，用来连接数据库
                username = i.user
                passwd = pc.decrypt(i.passwd)
                # passwd = i.passwd
                flag = False
                break
        if flag == False:
            break
    if 'username' in vars():
        res_set = mysql_query_set(sql, username, passwd, insname.ip, int(insname.port), dbname, limit_num)
        return res_set
    else:
        return (['PLEASE set the admin role account FIRST'], ''), ['error']


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

