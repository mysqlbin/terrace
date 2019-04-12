#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binlog2sql


def getdata():

    connection_settings = {'host': '192.168.0.54', 'port': 3306, 'user': 'admin', 'passwd': '123456abc', 'charset': 'utf8'}

    binname='mysql-bin.000063'
    begintime='2019-04-12 02:00:00'
    dbselected='sql_db'
    tbname='t1'


    version = 1
    if version == 1:
        flashback = True
    else:
        flashback = False



    sqltype = ['INSERT', 'UPDATE', 'DELETE']
    binlogsql = binlog2sql.Binlog2sql(connection_settings=connection_settings, start_file=binname,
                                          start_pos=4, end_file='', end_pos=0,
                                          start_time=begintime, stop_time='', only_schemas=dbselected,
                                          only_tables=tbname, no_pk=False, flashback=flashback, stop_never=False,
                                          back_interval=1.0, only_dml=False, sql_type=sqltype
                                      )
    binlogsql.process_binlog()
    sqllist = binlogsql.sqllist

    print(sqllist)


# def getdata():
#
#     print(1)

getdata()

