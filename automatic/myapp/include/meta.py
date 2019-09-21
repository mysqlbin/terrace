#!/bin/env python
#-*-coding:utf-8-*-
import pymysql
import sys,string,time,datetime
import logging
import traceback
from myapp.common.utils.aes_decryptor import Prpcrypt

logger = logging.getLogger('default')

def mysql_query(sql,user,passwd,host,port,dbname):
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
        result = ''
        column_list = ''
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
            # if i.role == 'admin':         '''获取账号和密码，用来连接数据库'''
            username = i.user
            passwd = pc.decrypt(i.passwd)
            flag = False
            break
        if flag == False:
            break
    if 'username' in vars():
        results, column_list, error = mysql_query(sql, username, passwd, insname.ip, int(insname.port), dbname)
        return results, column_list, error
    else:
        return (['PLEASE set the admin role account FIRST'], ''), ['error']



