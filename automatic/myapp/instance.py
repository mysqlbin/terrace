from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from myapp.include import meta
from myapp.include import function as func
from myapp.form import AddForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models.functions import Concat
from automatic import settings
from django.core import serializers
from myapp.models import Db_instance
from myapp.common.utils.rewrite_json_encoder import RewriteJsonEncoder


import datetime,time
import json
import os


def get_lists(request):

    """获取实例列表"""

    limit = int(request.POST.get('limit'))
    offset = int(request.POST.get('offset'))
    type = request.POST.get('type')
    db_type = request.POST.get('db_type')
    limit = offset + limit
    search = request.POST.get('search', '')

    instance_obj = Db_instance.objects.all()
    # 过滤搜索
    if search:
        instance_obj = instance_obj.filter(instance_name__icontains=search)
    # 过滤实例类型
    if type:
        instance_obj = instance_obj.filter(type__icontains=type)
    # 过滤数据库类型
    if db_type:
        instance_obj = instance_obj.filter(db_type=db_type)
    count = instance_obj.count()
    instance_res = instance_obj[offset:limit].values('id', 'instance_name', 'type', 'db_type', 'ip', 'port', )

    # QuerySet 序列化
    rows = [row for row in instance_res]
    result = {"total": count, "rows": rows}
    return HttpResponse(json.dumps(result),
                        content_type='application/json')

def get_instance_name_id(request):

    """获取所有实例的实例名称和ID编号"""

    instance_obj = Db_instance.objects.values('instance_name', 'id')
    rows = [row for row in instance_obj]
    res = {'status': 1, 'msg': 'ok', 'data': rows}
    return HttpResponse(json.dumps(res))


def get_instances_resource(request):
    """
   获取实例内的资源信息，database、schema、table、column
   :param request:
   :return:
   """
    resource_type = request.POST.get('resource_type')
    db_name = request.POST.get('db_name')
    schema_name = request.POST.get('schema_name')
    tb_name = request.POST.get('tb_name')

    insname = Db_instance.objects.get(id=int(request.POST.get('data_id')))

    result = {'status': 1, 'msg': 'ok', 'data': []}

    if resource_type == 'database':
        dbresult, col = meta.get_process_data(insname, 'show databases')
        resource = [row[0] for row in dbresult
                    if row[0] not in ('information_schema', 'performance_schema', 'mysql', 'test', 'sys')]

    elif resource_type == 'table':
        dbtable, col = meta.get_process_data(insname, 'show tables', db_name)
        resource = [row[0] for row in dbtable if row[0] not in ['test']]

    result['data'] = resource

    return HttpResponse(json.dumps(result), content_type='application/json')


def get_instances_binlog(request):

    result = {'status': 1, 'msg': 'ok', 'data': []}
    insname = Db_instance.objects.get(id=int(request.POST.get('data_id')))
    binlog, col = meta.get_process_data(insname, 'show binary logs')
    resource = [row for row in binlog]
    result['data'] = resource

    return HttpResponse(json.dumps(result), content_type='application/json')


def get_instance_users(request, id, instance_name):

    instance_name = instance_name
    try:
        insname = Db_instance.objects.get(id=int(id))
    except Db_instance.DoesNotExist:
       return HttpResponse('实例不存在')

    sql_get_user = '''select concat("\'", user, "\'", '@', "\'", host,"\'") as query from mysql.user;'''
    users_res, col = meta.get_process_data(insname, sql_get_user)

    # 获取用户权限信息
    res_user_priv = []
    for db_user in users_res:
        user_info = {}
        sql_get_permission        = 'show grants for {};'.format(db_user[0])
        user_priv, col            = meta.get_process_data(insname, sql_get_permission)
        user_info['user']        = db_user[0]
        user_info['privileges'] = user_priv
        res_user_priv.append(user_info)

    return render(request, 'users.html', locals())
