# from celery import task
import datetime
from django.contrib.auth.models import User
from myapp.include import binlog2sql
from myapp.include import binlog2sqlback
from django.core.mail import EmailMessage,send_mail,EmailMultiAlternatives
from django.template import loader
# from myapp.include.encrypt import prpcrypt
# from mypro.settings import EMAIL_SENDER


def parse_binlog_self(insname, binname, start_pos, stop_pos, begin_time, tbname, dbselected, flashback):

    flag = True

    for a in insname.db_name_set.all():
        for i in a.db_account_set.all():
            tar_username = i.user
            tar_passwd = i.passwd
            flag = False
            break
        if flag == False:
            break


    connection_settings = {'host': insname.ip, 'port': int(insname.port), 'user': tar_username, 'passwd': tar_passwd}

    sqltype = ['INSERT', 'UPDATE', 'DELETE']

    binlogsql = binlog2sqlback.Binlog2sql(connection_settings=connection_settings, start_file=binname,
                                          start_pos=start_pos, end_file='', end_pos=stop_pos,
                                          start_time=begin_time, stop_time='', only_schemas=dbselected,
                                          only_tables=tbname, no_pk=False, flashback=flashback, stop_never=False,
                                          back_interval=1.0, only_dml=False, sql_type=sqltype
                                          )
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



def parse_binlog_update(insname, binname, begintime, tbname, dbname, countnum):
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
                                      startTime=begintime, stopTime='', only_schemas=dbname,
                                      only_tables=tbname, nopk=False, flashback=False, stopnever=True,countnum=countnum)
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
