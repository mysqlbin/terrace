#!/usr/local/bin/python3
#coding=utf-8

import pymysql


def mysql_query(sql, user, passwd, host, port, get_data = 1):
    try:
        conn=pymysql.connect(host=host,user=user,passwd=passwd,port=int(port),connect_timeout=5,charset='utf8mb4')
        cursor = conn.cursor()
        cursor.execute(sql)
        if get_data == 1:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as err:
        return err

def get_process_data(insname, sql, get_data = 1):
    flag = True
    # pc = prpcrypt()
    #多对多的查询
    for a in insname.db_name_set.all():    #models.py：Db_name
        for i in a.db_account_set.all():   #models.py：Db_account
            # if i.role == 'admin':         '''获取账号和密码，用来连接数据库'''
            username = i.user
            passwd = i.passwd
            flag = False
            break
        if flag == False:
            break
    if 'username' in vars():
        try:
            #results = mysql_query('select 1', 'root', '123456abc', '192.168.0.54', 3306)
            results = mysql_query(sql, username, passwd, insname.ip, int(insname.port), get_data)
        except Exception as e:
            results = e
        return results
    else:
        return 'PLEASE set the admin role account FIRST'

def get_param_value(insname, param = ''):
    sql = "show global variables like '{:s}'".format(param)
    results = get_process_data(insname, sql)
    if results:
        res = '{} : {}'.format(results[0], results[1])
        return res

def get_status_value(insname, param = '',only_get_val = 1):
    sql = "show global status like '{:s}'".format(param)
    results = get_process_data(insname, sql)
    if results:
        if only_get_val == 1:
            res = '{} : {}'.format(results[0], results[1])
            return res
        else:
            res = results[1]
            return res

#0. too much columns indexes

def get_too_much_columns_indexs(insname, index_count = 5):
    """
    获取索引数目大于5个的表
    :param request:
    :param index_count 索引数目，默认为5
    :return:
    """
    # print("\033[1;33;44m 0: result of to much columns indexes\033[0m")
    sql = "select s.table_schema,s.table_name,s.index_name,s.column_name from information_schema.STATISTICS s, \
          (select table_name,index_name,count(*) from information_schema.STATISTICS where table_schema not in \
          ('information_schema','performance_schema','mysql','sys') group by table_name,index_name having \
          count(*)> {})t where s.table_name=t.table_name and s.index_name=t.index_name;" .format(index_count)
    results = get_process_data(insname, sql, 0)
    return results


# 1. talbe not has primary index
def get_not_primary_index(insname):

    print("\033[1;33;44m 1: result of table has not primary indexes\033[0m")
    sql = "SELECT t.table_schema,t.table_name FROM information_schema.tables AS t LEFT JOIN   \
        (SELECT DISTINCT table_schema, table_name FROM information_schema.`KEY_COLUMN_USAGE` ) AS kt ON \
        kt.table_schema=t.table_schema AND kt.table_name = t.table_name WHERE t.table_schema NOT IN \
        ('mysql', 'information_schema', 'performance_schema', 'sys') AND kt.table_name IS NULL;"

    results = get_process_data(insname, sql, 0)
    return results

#0 get table schema engine
def get_table_schema_engine(insname):
    """
    统计数据库实例存储引擎的类型的数量
    :param request
    :return:
    """
    print("\033[1;33;44m 0: result of group by engine type: \033[0m")
    sql = "select table_schema, engine, count(*) as engine_counts from information_schema.tables where table_schema not in \
           ('information_schema','mysql','performance_schema','sys') group by table_schema,engine;"
    results = get_process_data(insname, sql, 0)
    return results


def get_table_size(insname, val = 1):

    sql = "select table_schema,table_name,concat(round((data_length+index_length)/1024/1024,2),'M') as size, round((data_length+index_length)/1024/1024,2) as data FROM \
        information_schema.tables where (DATA_LENGTH+INDEX_LENGTH) > {}*1024*1024*1024  and table_schema not in \
        ('information_schema','mysql','performance_schema','sys') order by size desc".format(val)
    results = get_process_data(insname, sql, 0)
    return results

def get_top_big_tables(insname, limit = 20):

    sql = "SELECT table_schema,table_name,concat(round(data_length/1024/1024,2),'M') AS data_mb,concat(round(index_length/1024/1024,2), 'M') AS index_mb, \
                            concat(round((data_length + index_length)/1024/1024,2), 'M') AS all_mb,table_rows FROM \
                            information_schema.tables  where table_schema not in ('information_schema','mysql','performance_schema','sys') order by all_mb desc limit {}".format(limit)
    results = get_process_data(insname, sql, 0)
    return results

#3 get tables which have big fragment
def get_big_fragment_tables(insname, data_free = '0.1'):
    print("\033[1;33;44m 3: result of table has big fragment\033[0m")
    sql = "select table_schema,table_name,concat(round(DATA_FREE/1024/1024,2),'M') from information_schema.TABLES where table_schema not in \
          ('information_schema','mysql','performance_schema','sys') and data_free > {} *1024*1024*1024 order by DATA_FREE desc".format(data_free)
    results = get_process_data(insname, sql, 0)
    return results

#4 auto increment ratio
def get_auto_increment_ratio(instance, auto_increment_ratio = '0.3000'):

    print("\033[1;33;44m 4: result of auto increment ratio\033[0m")
    sql = "select table_schema,table_name,auto_increment_ratio,max_value,auto_increment from sys.schema_auto_increment_columns \
          where auto_increment_ratio > {} and table_schema not in \
          ('information_schema','mysql','performance_schema','sys') order by auto_increment_ratio desc".format(auto_increment_ratio)
    results = get_process_data(instance, sql, 0)
    return results

    if results:
        for val in results:
            print('table_schema:{:15s} table_name:{:30s} auto_increment_ratio:{} max_value:{} auto_increment:{}'.format(val[0], val[1], val[2], val[3], val[4]))
    else:
        print("no table auto increment ratio has more than {}...".format(auto_increment_ratio))


def get_table_rows(insname, table_rows = 20000000):
    """
     单表超过行数多少万的表
     :param request
     :return:
     """
    sql = "select table_schema,table_name,table_rows from \
         information_schema.TABLES where table_schema not in ('information_schema','mysql','performance_schema','sys') \
         and table_rows > {} order by table_rows desc;".format(table_rows)

    results = get_process_data(insname, sql, 0)
    return results

# 6.get tables which have big columns
def get_table_big_column(insname):

    sql = "select table_schema,table_name,column_name,data_type from information_schema.columns where data_type in \
          ('blob','clob','text','medium text','long text') and table_schema not in \
          ('information_schema','performance_schema','mysql','sys')"
    results = get_process_data(insname, sql, 0)
    return results

def get_table_long_varchar_column(insname, character_maximum_length = 500):

    sql="select table_schema,table_name,column_name,data_type,CHARACTER_MAXIMUM_LENGTH from information_schema.columns \
    where DATA_TYPE='varchar' and CHARACTER_MAXIMUM_LENGTH > {} and table_schema not in \
    ('information_schema','performance_schema','mysql','sys');".format(character_maximum_length)
    results = get_process_data(insname, sql, 0)
    return results


#long uncommitted transactions
def get_long_transactions(insname, time = 1):
    print("\033[1;33;44m result of long uncommitted transactions\033[0m")
    sql = "select pro.host, pro.user, pro.db, trx.trx_state, pro.COMMAND, concat(pro.time,'s') as runtime, trx.trx_id, pro.id as thread_id, trx.trx_query \
          from  information_schema.innodb_trx trx left join information_schema.PROCESSLIST pro on trx.trx_mysql_thread_id = pro.id where pro.time > {}".format(time)
    results = get_process_data(insname, sql, 0)
    return results

#tmp_tables, tmp_disk_tables
def get_sql_tmp_tables(insname, limit = 20):

    sql = "select db, tmp_tables, tmp_disk_tables, tmp_tables+tmp_disk_tables as tmp_all, last_seen, query from sys.statement_analysis \
          where tmp_tables>0 or tmp_disk_tables >0 order by tmp_all desc limit {};".format(limit)
    results = get_process_data(insname, sql, 0)
    return results


def get_version():
    sql = "select version()"
    results = get_process_data(sql)
    if results:
        return results[0]

def get_innodb_row_lock_current_waits(insname):
    sql = "show global status like 'Innodb_row_lock_current_waits'"
    results = get_process_data(insname, sql)
    if results:
        return results[1]

def get_innodb_lock_waits_list(insname):

    innodb_row_lock_current_waits = get_innodb_row_lock_current_waits(insname)
    if int(innodb_row_lock_current_waits) > 0:
        sql_version = "select version()"
        results = get_process_data(insname, sql_version)
        if results:
            get_version = results[0][0:3].replace('.','')
        else:
            get_version = 57

        if int(get_version) >= 57:
            sql  = "select locked_index,locked_type,blocking_lock_mode,waiting_lock_mode,waiting_query from sys.innodb_lock_waits"
            results = get_process_data(insname, sql, 0)
            return results
            # if results:
            #     for val in results:
            #         print('locked_index:{:10s} locked_type:{:10s} blocking_block_mode:{:10s} waiting_lock_mode:{:10s} waiting_query:{}'.format(val[0], val[1], val[2], val[3], val[4]))
            # else:
            #     print("no innodb row lock current waits list...")
        else:
            sql = "select requesting_trx_id,requested_lock_id,blocking_trx_id,blocking_lock_id from information_schema.innodb_lock_waits"
            results = get_process_data(insname, sql, 0)
            return results

            # return results
            # if results:
            #     for val in results:
            #         print('requesting_trx_id:{:10s} requested_lock_id:{:10s} blocking_trx_id:{:10s} blocking_lock_id:{} '.format(val[0], val[1], val[2], val[3]))
            # else:
            #     print("no innodb row lock current waits list...")


def get_instance_user_privileges():
    sql_get_user = '''select concat("\'", user, "\'", '@', "\'", host,"\'") as query from mysql.user;'''
    res = get_process_data(sql_get_user, 2)
    res_user_priv = []
    for db_user in res:
        user_info = {}
        sql_get_permission = 'show grants for {};'.format(db_user[0])
        user_priv = get_process_data(sql_get_permission, 2)
        user_info['user'] = db_user[0]
        user_info['privileges'] = user_priv
        res_user_priv.append(user_info)
    return res_user_priv


