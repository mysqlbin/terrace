# -*- coding: UTF-8 -*-
""" 
@author:
@file: binglog2sql.py
@time:
"""
# from common.config import SysConfig
from myapp.plugins.plugin import Plugin

from automatic import settings
__author__ = ''

class Binlog2Sql(Plugin):

    def __init__(self):
        self.path = settings.BINLOG2SQL_PATH
        # self.path = '/root/binlog2sql/binlog2sql/binlog2sql.py'
        self.required_args = []
        self.disable_args = []
        super(Plugin, self).__init__()    # 类继承

    def generate_args2cmd(self, args, shell):
        """
        转换请求参数为命令行
        :param args:
        :param shell:
        :return:
        """
        conn_options = ['conn_options']
        #解析模式
        parse_mode_options = ['stop-never', 'no-primary-key', 'flashback', 'back-interval']
        #解析范围控制
        range_options = ['start-file', 'start-position', 'stop-file', 'stop-position', 'start-datetime',
                         'stop-datetime']
        #对象过滤
        filter_options = ['databases', 'tables', 'only-dml', 'sql-type']

        if shell:
            cmd_args = f'python3 {self.path}' if self.path else ''
            for name, value in args.items():
                if name in conn_options:
                    cmd_args += f' {value}'
                elif name in parse_mode_options and value:
                    cmd_args += f' --{name}'
                elif name in range_options and value:
                    cmd_args += f" --{name}='{value}'"
                elif name in filter_options and value:
                    if name == 'only-dml':
                        cmd_args += f' --{name}'
                    else:
                        cmd_args += f' --{name} {value}'
        else:
            cmd_args = [self.path]
            for name, value in args.items():
                if name in conn_options:
                    cmd_args.append(f'{value}')
                elif name in parse_mode_options:
                    cmd_args.append(f'--{name}')
                elif name in range_options:
                    cmd_args.append(f'--{name}')
                    cmd_args.append(f'{value}')
                elif name in filter_options:
                    cmd_args.append(f'--{name}')
                    cmd_args.append(f'{value}')
        return cmd_args
