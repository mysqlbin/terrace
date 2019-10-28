# -*- coding: UTF-8 -*-
import logging
import os
import time
import traceback
import json
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
# from django_q.tasks import async_task
from myapp.common.utils.rewrite_json_encoder import RewriteJsonEncoder
from myapp.plugins.binglog2sql import Binlog2Sql
from myapp.models import Db_instance
# from sql.notify import notify_for_binlog2sql
from .tasks import binlog2sql_file
logger = logging.getLogger('default')

def binlog2sql(request):

    """
       通过解析binlog获取SQL
       :param request:
       :return:
    """

    result = {'status': 1, 'msg': 'ok', 'data': ''}

    try:
        instance = Db_instance.objects.get(id=int(request.POST.get('instance_id')))
    except Db_instance.DoesNotExist:
        result['status'] = 1
        result['msg'] = '实例不存在'
        return HttpResponse(json.dumps(result), content_type='application/json')

    save_sql = True if request.POST.get('save_sql') == 'true' else False
    no_pk = True if request.POST.get('no_pk') == 'true' else False
    flashback = True if request.POST.get('flashback') == 'true' else False
    back_interval = 0 if request.POST.get('back_interval') == '' else int(request.POST.get('back_interval'))
    num = 30 if request.POST.get('num') == '' else int(request.POST.get('num'))
    start_file = request.POST.get('start_file')
    start_pos = request.POST.get('start_pos') if request.POST.get('start_pos') == '' else int(request.POST.get('start_pos'))
    end_file = request.POST.get('end_file')
    end_pos = request.POST.get('end_pos') if request.POST.get('end_pos') == '' else int(request.POST.get('end_pos'))
    stop_time = request.POST.get('stop_time')
    start_time = request.POST.get('start_time')
    only_schemas = request.POST.getlist('only_schemas')
    only_tables = request.POST.getlist('only_tables[]')
    only_dml = True if request.POST.get('only_dml') == 'true' else False
    sql_type = ['INSERT', 'UPDATE', 'DELETE'] if request.POST.getlist('sql_type[]') == [] else request.POST.getlist(
        'sql_type[]')

    # flashback=True获取DML回滚语句
    result = {'status': 1, 'msg': 'ok', 'data': ''}

    # 提交给binlog2sql进行解
    binlog2sql = Binlog2Sql()
    # 准备参数
    args = {"conn_options": fr"-h{instance.host} -uroot -p123456abc -P{instance.port} ",
           "stop_never": False,
            "no-primary-key": no_pk,
            "flashback": flashback,
            "back-interval": back_interval,
            "start-file": start_file,
            "start-position": start_pos,
            "stop-file": end_file,
            "stop-position": end_pos,
            "start-datetime": start_time,
            "stop-datetime": stop_time,
            "databases": ' '.join(only_schemas),
            "tables": ' '.join(only_tables),
            "only-dml": only_dml,
            "sql-type": ' '.join(sql_type),
            "instance_ip": instance.host,
            "instance_name": instance.instance_name,
    }

    # 参数检查
    args_check_result = binlog2sql.check_args(args)

    if args_check_result['status'] == 0:
        return HttpResponse(json.dumps(args_check_result), content_type='application/json')
    # 参数转换
    cmd_args = binlog2sql.generate_args2cmd(args, shell=True)

    # 执行命令, 对binlog进行解析并返回
    try:
        p = binlog2sql.execute_cmd(cmd_args, shell=True)
        # 读取前num行后结束
        rows = []
        n = 1
        for line in iter(p.stdout.readline, ''):
            """
            line = INSERT INTO `test`.`test3`(`addtime`, `data`, `id`) VALUES ('2016-12-10 13:03:38', 'english', 4); #start 981 end 1147
           """
            if n <= num:
                n = n + 1
                row_info = {}
                try:
                    row_info['sql'] = line.split('; #')[0] + ";"
                    row_info['binlog_info'] = line.split('; #')[1].rstrip('\"')
                except IndexError:
                    row_info['sql'] = line
                    row_info['binlog_info'] = None
                rows.append(row_info)
            else:
                break
        if rows.__len__() == 0:
            # 判断是否有异常
            stderr = p.stderr.read()
            if stderr:
                result['status'] = 0
                result['msg'] = stderr
                return HttpResponse(json.dumps(result), content_type='application/json')
        # 终止子进程
        p.kill()
        result['data'] = rows
    except Exception as e:
        logger.error(traceback.format_exc())
        result['status'] = 0
        result['msg'] = str(e)

    # 异步保存到文件
    if save_sql:
        # binlog2sql_file(args=args)
        binlog2sql_file.delay(args=args)    #这里要加返回结果的判断，比如是否返回数据成功

    # 返回查询结果
    return HttpResponse(json.dumps(result), content_type='application/json')
    """
    {"status": 0, "msg": "ok", "data": [{"sql": "INSERT INTO `db1`.`accountinfo`(`AccountId`, `Ip`) VALUES (1, '1');", "binlog_info": "start 973 end 1208 time 2019-08-30 03:52:27\n"}]}
    """


# def binlog2sql_file(args):
#     """
#     用于异步保存binlog解析的文件
#     :param args: 参数
#     :param user: 操作用户对象，用户消息推送
#     :return:
#     """
#     binlog2sql = Binlog2Sql()
#     # instance = args.get('instance')
#     timestamp = int(time.time())
#
#     path = os.path.join(settings.BASE_DIR, 'downloads/polling/')
#     filename = os.path.join(path, f"{instance_name}的巡检报告{timestamp}.sql")
#
#
#     path = os.path.join(settings.BASE_DIR, 'downloads/binlog2sql/')
#     # if args.get('flashback'):
#     #     filename = os.path.join(path, f"flashback_{instance.host}_{instance.port}_{timestamp}.sql")
#     # else:
#     #     filename = os.path.join(path, f"{instance.host}_{instance.port}_{timestamp}.sql")
#     if args.get('flashback'):
#         filename = os.path.join(path, f"flashback__{timestamp}.sql")
#     else:
#         filename = os.path.join(path, f"{timestamp}.sql")
#
#     # 参数转换
#     cmd_args = binlog2sql.generate_args2cmd(args, shell=True)
#     # 执行命令保存到文件
#     with open(filename, 'w') as f:
#         p = binlog2sql.execute_cmd(cmd_args, shell=True)
#         for c in iter(p.stdout.readline, ''):
#             f.write(c)
#     # return user, filename
