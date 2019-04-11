# from celery import task
import datetime
from django.contrib.auth.models import User
from myapp.include import binlog2sql
from myapp.include import binlog2sqlback
from django.core.mail import EmailMessage,send_mail,EmailMultiAlternatives
from django.template import loader
# from myapp.include.encrypt import prpcrypt
# from mypro.settings import EMAIL_SENDER


def parse_binlog_self(insname, binname, begintime, tbname, dbselected):

    flag = True

    for a in insname.db_name_set.all():
        for i in a.db_account_set.all():
            tar_username = i.user
            tar_passwd = i.passwd
            flag = False
            break
        if flag == False:
            break

    #connectionSettings = {'host': '127.0.0.1', 'port': 3306, 'user': 'salt_user', 'passwd': '123456abc'}
    connection_settings = {'host': insname.ip, 'port': int(insname.port), 'user': tar_username, 'passwd': tar_passwd}
    '''
    def __init__(self, connection_settings, start_file=None, start_pos=None, end_file=None, end_pos=None,
                 start_time=None, stop_time=None, only_schemas=None, only_tables=None, no_pk=False,
                 flashback=False, stop_never=False, back_interval=1.0, only_dml=True, sql_type=None):
    '''
    '''
    binlog2sql = Binlog2sql(connection_settings=conn_setting, start_file=args.start_file, start_pos=args.start_pos,
                            end_file=args.end_file, end_pos=args.end_pos, start_time=args.start_time,
                            stop_time=args.stop_time, only_schemas=args.databases, only_tables=args.tables,
                            no_pk=args.no_pk, flashback=args.flashback, stop_never=args.stop_never,
                            back_interval=args.back_interval, only_dml=args.only_dml, sql_type=args.sql_type)
    '''
    binlogsql = binlog2sqlback.Binlog2sql(connection_settings=connection_settings, start_file=binname,
                                          start_pos=4, end_file='', end_pos=0,
                                          start_time=begintime, stop_time='', only_schemas=dbselected,
                                      only_tables=tbname, no_pk=False, flashback=False, stop_never=False)
    binlogsql.process_binlog()

    sqllist = binlogsql.sqllist

    return sqllist

def parse_binlog(insname,binname,begintime,tbname,dbselected,username,countnum,flash_back):
    flag = True
    # pc = prpcrypt()
    connectionSettings = {'host': '192.168.0.54', 'port': 3306, 'user': 'root', 'passwd': '123456abc'}
    #connectionSettings = {'host': insname.ip, 'port': int(insname.port), 'user': tar_username, 'passwd': tar_passwd}
    binlogsql = binlog2sql.Binlog2sql(connectionSettings=connectionSettings, startFile=binname,
                                      startPos=4, endFile='', endPos=0,
                                      startTime=begintime, stopTime='', only_schemas=dbselected,
                                      only_tables=tbname, nopk=False, flashback=flash_back, stopnever=False,countnum=countnum)
    binlogsql.process_binlog()
    sqllist = binlogsql.sqllist
    #sendmail_sqlparse.delay(username, dbselected, tbname, sqllist,flash_back)



def parse_binlog_update(insname, binname, begintime, tbname, dbselected, countnum):
    flag = True

    for a in insname.db_name_set.all():
        for i in a.db_account_set.all():
            tar_username = i.user
            tar_passwd = i.passwd
            flag = False
            break
        if flag == False:
            break
    #connectionSettings = {'host': '127.0.0.1', 'port': 3306, 'user': 'salt_user', 'passwd': '123456abc'}
    connectionSettings = {'host': insname.ip, 'port': int(insname.port), 'user': tar_username, 'passwd': tar_passwd}
    binlogsql = binlog2sql.Binlog2sql(connectionSettings=connectionSettings, startFile=binname,
                                      startPos=4, endFile='', endPos=0,
                                      startTime=begintime, stopTime='', only_schemas=dbselected,
                                      only_tables=tbname, nopk=True, flashback=True, stopnever=True,countnum=countnum)
    binlogsql.process_binlog()
    sqllist = binlogsql.sqllist
    return sqllist


def parse_binlogfirst(insname,binname,countnum):
    flag = True
    # pc = prpcrypt()
    #for a in insname.db_name_set.all():
        #for i in a.db_account_set.all():
            #if i.role == 'admin':
                #tar_username = i.user
                #tar_passwd = pc.decrypt(i.passwd)
                #flag = False
                #break
        #if flag == False:
            #break
    connectionSettings = {'host': '127.0.0.1', 'port': 3306, 'user': 'salt_user', 'passwd': '123456abc'}
    binlogsql = binlog2sql.Binlog2sql(connectionSettings=connectionSettings, startFile=binname,
                                      startPos=4, endFile='', endPos=0,
                                      startTime='', stopTime='', only_schemas='',
                                      only_tables='', nopk=False, flashback=False, stopnever=False,countnum=countnum)
    binlogsql.process_binlog()
    sqllist = binlogsql.sqllist
    return sqllist




# def task_run(idnum,request):
#     while 1:
#         try:
#             task = Task.objects.get(id=idnum)
#         except:
#             continue
#         break
#     if task.status!='executed' and task.status!='running' and task.status!='NULL':
#         hosttag = task.dbtag
#         sql = task.sqltext
#         mycreatetime = task.create_time
#         incept.log_incep_op(sql,hosttag,request,mycreatetime)
#         status='running'
#         task.status = status
#         task.operator  = request.user.username
#         task.update_time = datetime.datetime.now()
#         task.save()
#         process_runtask.delay(hosttag,sql,task)
#         return ''
#     elif task.status=='NULL':
#         return 'PLEASE CHECK THE SQL FIRST'
#     else:
#         return 'Already executed or in running'
