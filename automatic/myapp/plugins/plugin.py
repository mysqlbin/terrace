# -*- coding: UTF-8 -*-
""" 
@author:
@license: Apache Licence 
@file: plugin.py 
@time: 2019/03/04
"""

import logging
import subprocess
import traceback

logger = logging.getLogger('default')


class Plugin:
    def __init__(self, path):
        self.path = path
        self.required_args = []  # 必须参数
        self.disable_args = []  # 禁用参数

    def check_args(self, args):
        """
        检查请求参数列表
        :return: {'status': 1, 'msg': 'ok', 'data': {}}
        """

        args_check_result = {'status':0, 'msg': 'ok', 'data': {}}

        # 检查路径
        if self.path is None:
            args_check_result['msg'] = '可执行文件路径不能为空！'

        # 检查禁用参数
        for arg in args.keys():
            if arg in self.disable_args:
                args_check_result['msg'] = '参数已被禁用'.format(arg)
        # 检查必须参数
        for req_arg in self.required_args:
            if req_arg not in args.keys():
                args_check_result['msg'] = '必须指定{}参数'.format(req_arg)
            elif args[req_arg] is None or args[req_arg] == '':
                args_check_result['msg'] = '{}参数值不能为空'.format(req_arg)
        return args_check_result

    @staticmethod
    def execute_cmd(cmd_args, shell):
        """
        执行命令并且返回process
        :return:
        """
        try:
            p = subprocess.Popen(cmd_args,
                                 shell=shell,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True)
            return p
        except Exception as e:
            logger.error("命令执行失败\n{}".format(traceback.format_exc()))
            raise RuntimeError('命令执行失败，失败原因:%s' % str(e))     #通过raise error中断程序的执行
