# from celery import task
import time
import os
from django.conf import settings
from myapp.plugins.binglog2sql import Binlog2Sql
from celery import shared_task

def binlog2sql_file(args):
    """
    用于异步保存binlog解析的文件
    :param args: 参数
    :return:
    """
    binlog2sql = Binlog2Sql()

    path = os.path.join(settings.BASE_DIR, 'downloads/binlog2sql/')
    # if args.get('flashback'):
    #     filename = os.path.join(path, f"flashback_{instance.host}_{instance.port}_{timestamp}.sql")
    # else:
    #     filename = os.path.join(path, f"{instance.host}_{instance.port}_{timestamp}.sql")
    if args.get('flashback'):
        filename = os.path.join(path, f"flashback__{timestamp}.sql")
    else:
        filename = os.path.join(path, f"{timestamp}.sql")

    # 参数转换
    cmd_args = binlog2sql.generate_args2cmd(args, shell=True)
    # 执行命令保存到文件
    with open(filename, 'w') as f:
        p = binlog2sql.execute_cmd(cmd_args, shell=True)
        for c in iter(p.stdout.readline, ''):
            f.write(c)

