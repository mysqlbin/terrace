#!/bin/env python
#-*-coding:utf-8-*-
import pymysql
import sys,string,time,datetime

def mysql_query(sql,user,passwd,host,port,dbname):

    conn=pymysql.connect(host=host,user=user,passwd=passwd,port=int(port),connect_timeout=5,charset='utf8')
    conn.select_db(dbname)
    cursor = conn.cursor()
    count=cursor.execute(sql)
    index=cursor.description
    col=[]
    #get column name

    for i in index:
        col.append(i[0])
    result=cursor.fetchall()
    # result=cursor.fetchmany(size=int(limitnum))
    cursor.close()
    conn.close()
    return (result,col)




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


# def get_process_data(insname,sql):
#
#     results,col = mysql_query(sql,'salt_user','123456abc','127.0.0.1',3306,'information_schema')
#
#     return results,col

def get_process_data(insname,sql):
    flag = True
    # pc = prpcrypt()
    for a in insname.db_name_set.all():
        for i in a.db_account_set.all():
            # if i.role == 'admin':
            tar_username = i.user
            tar_passwd = i.passwd
            flag = False
            break
        if flag == False:
            break
    if 'tar_username' in vars():
        try:
            results, col = mysql_query(sql,tar_username,tar_passwd,insname.ip,int(insname.port),'information_schema')
        except Exception as e:
            #防止失败，返回一个wrong_message
            results, col = ([str(e)], ''), ['error']
            #results,col = mysql_query(wrong_msg,user,passwd,host,int(port),dbname)
        return results, col
    else:
        return (['PLEASE set the admin role account FIRST'], ''), ['error']

'''
sql = "select * from mon_tbsize where DBTAG='" + dbtag + "' order by `TOTAL(M)` desc "
'''
