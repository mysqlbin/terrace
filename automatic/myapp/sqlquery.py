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
from myapp.models import Db_instance, Query_log
from myapp.engines import get_engine
from myapp.engines.models import ResultsSet

from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import F,Max,Sum,Value as V
from django.db.models.functions import Concat
from automatic import settings

from django.core import serializers

from myapp.common.utils.rewrite_json_encoder import RewriteJsonEncoder
from django_q.tasks import async_task, result, fetch

import datetime,time
import json

logger = logging.getLogger('default')

def sql_query_asynchronous(request):
    """
    获取SQL的查询结果
    :param request:
    :return:
    """
    instance_id = request.POST.get('instance_id')
    instance_name = request.POST.get('instance_name')
    sql_content = request.POST.get('sql_content')
    db_name = request.POST.get('db_name')
    limit_num = int(request.POST.get('limit_num'))

    res = {'status': 0, 'msg': 'ok', 'data': {}}

    # instance_name = '1'
    # sql_content = 'select nPlayerID from niuniu_db.table_award_2019;'
    # db_name = 'niuniu_db'
    # limit_num=2

    try:
        instance = Db_instance.objects.get(id=int(instance_id))
    except Db_instance.DoesNotExist:
        res['status'] = 1
        res['msg'] = '实例不存在'
        return HttpResponse(json.dumps(res), content_type='application/json')

    # 服务器端参数验证
    if not instance_name or not sql_content or not db_name or not limit_num:
        res['status'] = 1
        res['instance_name'] = instance_name
        res['sql_content'] = sql_content
        res['db_name'] = db_name
        res['msg'] = '提交参数可能为空'
        return HttpResponse(json.dumps(res), content_type='application/json')

    # show、explain语句的 limit 要改为0
    if re.match("show|explain", sql_content) is not None:
        limit_num = 0

    try:
        query_engine = get_engine(instance=instance)
        query_check_info = query_engine.query_check(sql=sql_content)
        if query_check_info.get('bad_query'):
            res['status'] = 1
            res['msg'] = query_check_info.get('msg')
            return HttpResponse(json.dumps(res), content_type='application/json')

        if query_check_info.get('has_star'):
            res['status'] = 1
            res['msg'] = query_check_info.get('msg')
            return HttpResponse(json.dumps(res), content_type='application/json')

        #　执行查询语句，获取返回结果
        # 异步
        max_execution_time = settings.MAX_EXECUTION_TIME
        task_id = async_task(query_engine.query_set, sql=sql_content, db_name=db_name, limit_num=limit_num)
        query_task = fetch(task_id, wait=max_execution_time * 1000)

        if query_task:
            if query_task.success:
                query_result = query_task.result
                query_result.rows = query_result.to_dict()   # 访问类的成员函数
                query_result.query_time = query_task.time_taken()
            else:
                query_result = ResultsSet(full_sql=sql_content)
                query_result.error = query_task.result
        # 等待超时，async_task主动关闭连接
        else:
            query_result = ResultsSet(full_sql=sql_content)
            query_result.error = f'查询时间超过 {max_execution_time} 秒，已被主动终止，请优化语句或者联系管理员。'

        if query_result.error:
            res['status'] = 1
            res['msg'] = query_result.error
            res['abc'] = 'test'

        else:
            res['data'] = query_result.__dict__

        # 仅将成功的查询语句记录存入数据库
        if not query_result.error:
            query_log = Query_log(
                user          = request.user.username,
                instance_id   = instance_id,
                instance_name = instance_name,
                dbname        = db_name,
                sqlcontent    = sql_content,
                query_time    = query_result.query_time,
                effect_row    = query_result.effect_row
            )
            query_log.save()


    except Exception as e:

        logger.error(f'查询异常报错，查询语句：{sql_content}\n，错误信息：{traceback.format_exc()}')
        res['status'] = 1
        res['msg'] = f'查询异常报错，错误信息：{e}'

    # 返回查询结果

    return HttpResponse(json.dumps(res, cls=RewriteJsonEncoder),content_type='application/json')

