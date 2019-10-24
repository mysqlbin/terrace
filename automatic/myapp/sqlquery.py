# -*- coding: UTF-8 -*-
import logging
import traceback
import re

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.include import meta
from myapp.include import function as func
from myapp.include import sqlfilter
from myapp.form import AddForm
from myapp.models import Db_instance
from myapp.engines import get_engine

from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import F,Max,Sum,Value as V
from django.db.models.functions import Concat
from automatic import settings

from django.core import serializers

from myapp.common.utils.rewrite_json_encoder import RewriteJsonEncoder
from django_q.tasks import async_task, result


import datetime,time
import json

logger = logging.getLogger('default')

def sql_query(request):
    """
    获取SQL的查询结果
    :param request:
    :return:
    """

    instance_name = request.POST.get('instance_name')
    sql_content = request.POST.get('sql_content')
    db_name = request.POST.get('db_name')
    limit_num = int(request.POST.get('limit_num'))

    res = {'status': 0, 'msg': 'ok', 'rows': [], 'column_list': []}

    # instance_name = '1'
    # sql_content = 'select nPlayerID from niuniu_db.table_award_2019;'
    # db_name = 'niuniu_db'
    # limit_num=2

    try:
        instance = Db_instance.objects.get(id=int(request.POST.get('instance_id')))
    except Db_instance.DoesNotExist:
        res['status'] = 1
        res['msg'] = '实例不存在'
        res['rows'] = '{1}'
        return HttpResponse(json.dumps(result), content_type='application/json')

    # 服务器端参数验证
    if not instance_name or not sql_content or not db_name or not limit_num:
        res['status'] = 1
        res['instance_name'] = instance_name
        res['sql_content'] = sql_content
        res['db_name'] = db_name
        res['msg'] = '提交参数可能为空'
        res['rows'] = '{2}'
        return HttpResponse(json.dumps(result), content_type='application/json')

    # show、explain语句的 limit 要改为0
    if re.match("show|explain", sql_content) is not None:
        limit_num = 0

    try:
        query_engine = get_engine(instance=instance)
        query_check_info = query_engine.query_check(sql=sql_content)
        if query_check_info.get('bad_query'):
            res['status'] = 1
            res['msg'] = query_check_info.get('msg')
            res['rows'] = '{3}'

            return HttpResponse(json.dumps(result), content_type='application/json')

        if query_check_info.get('has_star'):
            res['status'] = 1
            res['msg'] = query_check_info.get('msg')
            res['rows'] = '{4}'
            return HttpResponse(json.dumps(result), content_type='application/json')

        #　执行查询语句，获取返回结果
        # 非异步
        res_set = query_engine.query_set(sql=sql_content, limit_num=limit_num)
        # 异步
        # task_id = async_task(query_engine.query_set(sql=sql_content, limit_num=limit_num))
        # task_result = result(task_id, wait=1 * 100, cached=True)


        if res_set.error:
            res['status'] = 1
            res['msg'] = res_set.error
            res['rows'] = '{6}'
            return HttpResponse(json.dumps(result), content_type='application/json')

        res['rows'] = res_set.to_dict()    # 访问类的成员函数
        res['column_list'] = res_set.column_list

    except Exception as e:

        logger.error(f'查询异常报错，查询语句：{sql_content}\n，错误信息：{traceback.format_exc()}')
        res['status'] = 1
        res['msg'] = f'查询异常报错，错误信息：{e}'

    # 返回查询结果
    try:
        return HttpResponse(json.dumps(res, cls=RewriteJsonEncoder),
                            content_type='application/json')
    except Exception as err:

        return HttpResponse(err)

