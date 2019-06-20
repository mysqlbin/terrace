# from celery import task
import datetime
from django.contrib.auth.models import User
from myapp.include import binlog2sql
from django.core.mail import EmailMessage,send_mail,EmailMultiAlternatives
from django.template import loader
# from myapp.include.encrypt import prpcrypt
# from mypro.settings import EMAIL_SENDER


def parse_to_binlog2sql(insname, binname, start_pos, stop_pos, begin_time, tbname, dbselected, flashback, countnum):

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

    binlogsql = binlog2sql.Binlog2sql(connection_settings=connection_settings, start_file=binname,
                                          start_pos=start_pos, end_file='', end_pos=stop_pos,
                                          start_time=begin_time, stop_time='', only_schemas=dbselected,
                                          only_tables=tbname, no_pk=False, flashback=flashback, stop_never=False,
                                          back_interval=1.0, only_dml=False, sql_type=sqltype, countnum=countnum
                                          )
    binlogsql.process_binlog()
    sqllist = binlogsql.sqllist
    return sqllist

