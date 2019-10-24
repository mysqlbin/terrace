# from celery import task
import time
import os
from django.conf import settings
from myapp.plugins.binglog2sql import Binlog2Sql
from celery import shared_task

@shared_task()
def binlog2sql_file(args):
    """
    用于异步保存binlog解析的文件
    :param args: 参数
    :return:
    """
    instance_ip   = args.get('instance_ip')
    instance_name = args.get('instance_name')
    timestamp = int(time.time())

    binlog2sql = Binlog2Sql()

    path = os.path.join(settings.BASE_DIR, 'downloads/binlog2sql/')
    if args.get('flashback'):
        filename = os.path.join(path, f"flashback_{instance_ip}_{instance_name}_{timestamp}.sql")
    else:
        filename = os.path.join(path, f"{instance_ip}_{instance_name}_{timestamp}.sql")

    # 参数转换
    cmd_args = binlog2sql.generate_args2cmd(args, shell=True)
    # 执行命令保存到文件
    with open(filename, 'w') as f:
        p = binlog2sql.execute_cmd(cmd_args, shell=True)
        for c in iter(p.stdout.readline, ''):
            f.write(c)

