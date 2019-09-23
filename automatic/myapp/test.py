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

def get_query_data(request):

    sql = 'show bin1ary logs;'
    host = '192.168.0.54'
    user = 'root'
    passwd = '123456abc'
    port = 3306
    data, col = mysql_query(sql, user, passwd, host, port, 'mysql')

    # return HttpResponse(data)

    """
    ('mysql-bin.000001', 201)('mysql-bin.000002', 3650)('mysql-bin.000003', 1333)('mysql-bin.000004', 1333)('mysql-bin.000005', 9512)('mysql-bin.000006', 27595)
    """
    return HttpResponse(col)
    """
    ['Log_name', 'File_size']
    """
