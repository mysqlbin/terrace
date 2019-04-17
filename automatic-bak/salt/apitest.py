# coding=utf-8
import ssl,pymysql,socket
import urllib,json
import urllib.request
import urllib.parse
import datetime
class SaltAPI(object):
    ssl._create_default_https_context = ssl._create_unverified_context
    # SALT_API_URL = 'https://192.168.1.26:8888/'
    # SALT_API_USER = 'saltapi'
    # SALT_API_PASSWD = 'saltapi'
    def __init__(self):
        self.__url = 'https://192.168.1.26:8888/'
        self.__user = 'saltapi'
        self.__password = 'saltapi'
        self.__token_id = self.saltLogin()

    def saltLogin(self):
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}

        encode = urllib.parse.urlencode(params)
        obj = urllib.parse.unquote(encode).encode('utf-8')

        headers = {'X-Auth-Token': ''}
        url = self.__url + '/login'
        req = urllib.request.Request(url, obj, headers)
        opener = urllib.request.urlopen(req)
        content = json.loads(opener.read())

        try:
            token = content['return'][0]['token']
            return token
        except KeyError:
            raise KeyError

    def postRequest(self, obj, prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token': self.__token_id}
        req = urllib.request.Request(url, obj, headers)
        opener = urllib.request.urlopen(req)
        content = json.loads(opener.read())
        return content

    # ok
    def asyncMasterToMinion(self,  tgt, fun, arg, group=0):

        if tgt == '*':
            params = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'arg': arg, 'ret': 'mysql'}
        else:
            if group == 1:
                params = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': 'nodegroup',
                          'ret': 'mysql'}
            else:
                sapi_1 = SaltAPI()
                if sapi_1.is_valid_ip(tgt):
                    params = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': 'ipcidr',
                              'ret': 'mysql'}
                else:
                    params = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': 'list',
                              'ret': 'mysql'}

        obj = urllib.parse.urlencode(params).encode('utf-8')

        content = self.postRequest(obj)

        jid = content['return'][0]['jid']

        return jid

    def get_host_list(self, se_host, isgp):
        sapi_1 = SaltAPI()

        if se_host == '*':
            return sapi_1.runner_status('status')['up']
        else:
            if isgp == 1:
                x = sapi_1.remote_noarg_execution_mul(se_host, 'test.ping', 1)
                return x
            else:
                x, y = sapi_1.remote_noarg_execution_mul(se_host, 'test.ping')
                return x

    def runner_status(self, arg):
        ''' Return minion status '''
        params = {'client': 'runner', 'fun': 'manage.' + arg}
        obj = urllib.parse.urlencode(params).encode('utf-8')
        content = self.postRequest(obj)['return'][0]
        return content
    #remote_noarg_execution_mul(se_host, 'test.ping', 1)
    def remote_noarg_execution_mul(self, tgt, fun, group=0):
        ''' Execute commands without parameters '''
        if tgt == '*':
            params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'ret': 'mysql'}
        else:
            if group == 1:
                #return '111333'
                params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'ret': 'mysql', 'expr_form': 'nodegroup'}
            else:
                sapi_1 = SaltAPI()
                if sapi_1.is_valid_ip(tgt):
                    params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'ret': 'mysql', 'expr_form': 'ipcidr'}
                else:
                    params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'ret': 'mysql', 'expr_form': 'list'}
        return params
        #obj = urllib.parse.urlencode(params).encode('utf-8')
        #return obj
        #content = self.postRequest(obj)
        #return content
        #return content['return'][0].keys(), content['return'][0].values()

    def is_valid_ip(self, ip):
        """Returns true if the given string is a well-formed IP address.

        Supports IPv4 and IPv6.
        """
        if not ip or '\x00' in ip:
            # getaddrinfo resolves empty strings to localhost, and truncates
            # on zero bytes.
            return False
        try:
            res = socket.getaddrinfo(ip, 0, socket.AF_UNSPEC,
                                     socket.SOCK_STREAM,
                                     0, socket.AI_NUMERICHOST)
            return bool(res)
        except socket.gaierror as e:
            if e.args[0] == socket.EAI_NONAME:
                return False
            raise
        return True

    # 定义不加参数的命令
    def remote_noarg_execution_sin(self, tgt, fun):
        ''' Execute commands without parameters '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'ret': 'mysql'}
        obj = urllib.parse.urlencode(params).encode('utf-8')
        content = self.postRequest(obj)
        ret = content['return'][0][tgt]
        return ret



    # 定义获取所有客户端KEY函数
    def list_all_key(self):
        '''
           返回所有Minion keys；
           分别为 已接受、待接受、已拒绝；
           :return: [u'local', u'minions_rejected', u'minions_denied', u'minions_pre', u'minions']
       '''
        params = {'client': 'wheel', 'fun': 'key.list_all'}
        obj = urllib.parse.urlencode(params).encode('utf-8')
        content = self.postRequest(obj)
        # minions = content['return'][0]['data']['return']['minions']
        # minions_pre = content['return'][0]['data']['return']['minions_pre']
        # minions_rej = content['return'][0]['data']['return']['minions_rejected']
        # minions_den = content['return'][0]['data']['return']['minions_denied']
        minions = content['return'][0]['data']['return']
        return minions

    def delete_key(self, node_name):
        params = {'client': 'wheel', 'fun': 'key.delete', 'match': node_name}
        obj = urllib.parse.urlencode(params).encode('utf-8')
        content = self.postRequest(obj)
        ret = content['return'][0]['data']['success']
        return ret

    def accept_key(self, node_name):
        params = {'client': 'wheel', 'fun': 'key.accept', 'match': node_name}
        obj = urllib.parse.urlencode(params).encode('utf-8')
        content = self.postRequest(obj)
        ret = content['return'][0]['data']['success']
        return ret

    def reject_key(self, node_name):
        params = {'client': 'wheel', 'fun': 'key.reject', 'match': node_name}
        obj = obj = urllib.parse.urlencode(params).encode('utf-8')
        content = self.postRequest(obj)
        ret = content['return'][0]['data']['success']
        return ret

def main():
    # 以下是用来测试saltAPI类的部分

    sapi = SaltAPI()
    # return HttpResponse(333)
    up_host = sapi.get_host_list('group1', 1)

    info_all = sapi.remote_noarg_execution_sin(up_host, 'grains.items')

    print(info_all)
    # params = {'client': 'local', 'fun': 'run.cmd', 'tgt': '*'}
    # params = {'client':'local', 'fun':'test.ping', 'tgt':'某台服务器的key'}
    # params = {'client':'local', 'fun':'test.echo', 'tgt':'某台服务器的key', 'arg1':'hello'}
    # params = {'client':'local', 'fun':'test.ping', 'tgt':'group1', 'expr_form':'nodegroup'}
    # test = sapi1.saltCmd(params)
    # print("params)
    #asyncMasterToMinion(self, tgt, fun, arg, group=0)
    #print(sapi1.asyncMasterToMinion('group1','test.ping','none_arg', 1))
    # x= sapi1.list_all_key()
    # print(x)
    #
    # a = sapi1.runner_status('status')['up']
    # print a


if __name__ == '__main__':
    main()



