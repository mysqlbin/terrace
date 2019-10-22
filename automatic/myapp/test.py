from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.include import meta
from myapp.include import function as func
from myapp.include import sqlfilter
from myapp.form import AddForm
from myapp.models import Db_instance,SlowQuery,SlowQueryHistory

from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import F,Max,Sum,Value as V
from django.db.models.functions import Concat
from automatic import settings

from django.core import serializers

from myapp.common.utils.aes_decryptor import Prpcrypt


from myapp.common.utils.rewrite_json_encoder import RewriteJsonEncoder

import pymysql
import datetime,time
import json
import logging
import traceback

logger = logging.getLogger('default')




def mysql_query(sql,user,passwd,host,port,dbname):
    try:
        conn   = pymysql.connect(host=host,user=user,passwd=passwd,port=int(port),connect_timeout=5,charset='utf8mb4')
        conn.select_db(dbname)
        cursor = conn.cursor()
        cursor.execute(sql)
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
        logger.error(f"MySQL语句执行报错，语句：{sql}，错误信息{traceback.format_exc()}")
        # logger
        return ([str(e)],''), ['error']

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



def get_query_data(request):

    insname = Db_instance.objects.get(id=1)
    flag = True
    pc = Prpcrypt()

    # 多对多的查询
    # SELECT `myapp_db_name`.`id`, `myapp_db_name`.`dbtag`, `myapp_db_name`.`dbname` FROM `myapp_db_name` INNER JOIN `myapp_db_name_instance` ON (`myapp_db_name`.`id` = `myapp_db_name_instance`.`db_name_id`) WHERE `myapp_db_name_instance`.`db_instance_id` = 7; args=(7,)
    for a in insname.db_name_set.all():  # models.py：Db_name
        # SELECT `myapp_db_account`.`id`, `myapp_db_account`.`user`, `myapp_db_account`.`passwd`, `myapp_db_account`.`role`, `myapp_db_account`.`tags` FROM `myapp_db_account` INNER JOIN `myapp_db_account_dbname` ON (`myapp_db_account`.`id` = `myapp_db_account_dbname`.`db_account_id`) WHERE `myapp_db_account_dbname`.`db_name_id` = 2; args=(2,)
        for i in a.db_account_set.all():  # models.py：Db_account
            if i.role == 'admin':
                # 获取账号和密码，用来连接数据库
                username = i.user
                passwd = pc.decrypt(i.passwd)

                # passwd = i.passwd
                flag = False
                break
        if flag == False:
            break
    # return HttpResponse(passwd)
    return HttpResponse(username)
    sql = 'show database'
    dbname = 'db1'
    if 'username' in vars():
        results, column_list, error = mysql_query(sql, username, passwd, insname.ip, int(insname.port), dbname)
        return results, column_list, error
    else:
        return (['PLEASE set the admin role account FIRST'], ''), ['error']

    """
    ('mysql-bin.000001', 201)('mysql-bin.000002', 3650)('mysql-bin.000003', 1333)('mysql-bin.000004', 1333)('mysql-bin.000005', 9512)('mysql-bin.000006', 27595)
    """
    return HttpResponse(data)
    """
    ['Log_name', 'File_size']
    """
