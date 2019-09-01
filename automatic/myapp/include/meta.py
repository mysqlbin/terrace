#!/bin/env python
#-*-coding:utf-8-*-
import pymysql
import sys,string,time,datetime

def mysql_query(sql,user,passwd,host,port,dbname):
    try:
        conn   = pymysql.connect(host=host,user=user,passwd=passwd,port=int(port),connect_timeout=5,charset='utf8mb4')
        conn.select_db(dbname)
        cursor = conn.cursor()
        count  = cursor.execute(sql)
        index  = cursor.description
        col=[]
        #获取列名
        try:
            for i in index:
                col.append(i[0])
        except Exception as e:
            cursor.close()
            conn.close()
            return (['ok'], ''), ['set']

        result=cursor.fetchall()
        cursor.close()
        conn.close()
        return (result, col)
    except Exception as e:
        return ([str(e)],''), ['error']



def process(insname,flag=1,sql=''):
    if flag ==1:
        sql = 'select * from information_schema.processlist ORDER BY TIME DESC'
        return get_process_data(insname,sql)
    elif flag ==2:
        sql = "select * from information_schema.processlist where COMMAND!='Sleep' ORDER BY TIME DESC"
        return get_process_data(insname, sql)
    elif flag == 3:
        sql = "show engine innodb status"
        return get_process_data(insname, sql)
    elif flag == 5:
        sql = "show engine innodb mutex"
        return get_process_data(insname, sql)
    elif flag == 6:
        sql = "SELECT table_schema as 'DB',table_name as 'TABLE',CONCAT(ROUND(( data_length + index_length ) / ( 1024 * 1024 ), 2), '') 'TOTAL(M)' , table_comment as COMMENT FROM information_schema.TABLES ORDER BY data_length + index_length DESC limit 20;"
        return get_process_data(insname, sql)
    elif flag==7 :
        return get_process_data(insname, sql)
    elif flag == 8:
        sql = "select * from sys.schema_auto_increment_columns order by auto_increment_ratio desc limit 100"
        return get_process_data(insname, sql)


def get_process_data(insname,sql, dbname = 'information_schema'):
    flag = True
    # pc = prpcrypt()

    #多对多的查询
    #SELECT `myapp_db_name`.`id`, `myapp_db_name`.`dbtag`, `myapp_db_name`.`dbname` FROM `myapp_db_name` INNER JOIN `myapp_db_name_instance` ON (`myapp_db_name`.`id` = `myapp_db_name_instance`.`db_name_id`) WHERE `myapp_db_name_instance`.`db_instance_id` = 7; args=(7,)
    for a in insname.db_name_set.all():    #models.py：Db_name
        #SELECT `myapp_db_account`.`id`, `myapp_db_account`.`user`, `myapp_db_account`.`passwd`, `myapp_db_account`.`role`, `myapp_db_account`.`tags` FROM `myapp_db_account` INNER JOIN `myapp_db_account_dbname` ON (`myapp_db_account`.`id` = `myapp_db_account_dbname`.`db_account_id`) WHERE `myapp_db_account_dbname`.`db_name_id` = 2; args=(2,)
        for i in a.db_account_set.all():   #models.py：Db_account
            # if i.role == 'admin':         '''获取账号和密码，用来连接数据库'''
            username = i.user
            passwd = i.passwd
            flag = False
            break
        if flag == False:
            break
    # if 'username' in vars():
    try:
        results, col = mysql_query(sql, username, passwd, insname.ip, int(insname.port), dbname)
    except Exception as e:
        results, col = ([str(e)], ''), ['error']
    return results, col
    # else:
    #     return (['PLEASE set the admin role account FIRST'], ''), ['error']



