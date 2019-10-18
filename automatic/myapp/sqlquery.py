# -*- coding: UTF-8 -*-
import logging
import traceback

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.include import meta
from myapp.include import function as func
from myapp.include import sqlfilter
from myapp.form import AddForm
from myapp.models import Db_instance

from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import F,Max,Sum,Value as V
from django.db.models.functions import Concat
from automatic import settings

from django.core import serializers

from myapp.common.utils.rewrite_json_encoder import RewriteJsonEncoder

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
    limit_num = int(request.POST.get('limit_num', 0))

    result = {'status': 0, 'msg': 'ok', 'data': {}}

    try:
        insname = Db_instance.objects.get(id=int(request.POST.get('instance_id', 1)))
    except Db_instance.DoesNotExist:
        result['status'] = 1
        result['msg'] = '实例不存在'
        result['data'] = '{1}'
        return HttpResponse(json.dumps(result), content_type='application/json')

    instance_name = 1
    sql_content = 'select id1 from auth_user where id=1;'
    db_name = 'terrace_db'
    limit_num = 1
    # 服务器端参数验证
    if not instance_name or not sql_content or not db_name or not limit_num:
        result['status'] = 1
        result['msg'] = '提交参数可能为空'
        result['data'] = '{2}'
        return HttpResponse(json.dumps(result), content_type='application/json')

    try:
        query_check_info = meta.query_check(sql=sql_content)

        # return HttpResponse(query_check_info)

        if query_check_info.get('bad_query'):
            result['status'] = 1
            result['msg'] = query_check_info.get('msg')
            result['data'] = {3}
            return HttpResponse(json.dumps(result), content_type='application/json')

        if query_check_info.get('has_star'):
            result['status'] = 1
            result['msg'] = query_check_info.get('msg')
            result['data'] = '{4}'
            return HttpResponse(json.dumps(result), content_type='application/json')

        #　执行查询语句，获取返回结果
        data, col, error = meta.get_process_data(insname, sql_content, db_name)
        if error != '':
            result['status'] = 1
            result['msg'] = error
            result['data'] = '{6}'
            return HttpResponse(json.dumps(result), content_type='application/json')

    except Exception as e:

        logger.error(f'查询异常报错，查询语句：{sql_content}\n，错误信息：{traceback.format_exc()}')
        result['status'] = 1
        result['msg'] = f'查询异常报错，错误信息：{e}'

        return HttpResponse(json.dumps(result), content_type='application/json')

    # 返回查询结果

    return HttpResponse(json.dumps(result, cls=ExtendJSONEncoder, bigint_as_string=True),
                        content_type='application/json')

    return HttpResponse(111)
