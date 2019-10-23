#!/usr/local/bin/python3
#coding=utf-8


def get_table_schema_engine():
    """
    1.1 统计数据库存储引擎的数量
    :param request
    :return:
    """
    sql = "select table_schema, engine, count(*) as engine_counts from information_schema.tables where table_schema not in \
           ('information_schema','mysql','performance_schema','sys') group by table_schema,engine;"
    return sql

def get_table_size(value=1):
    """
    1.2 超过多少G的大表,默认为1G
    :param value:
    :return:
    """
    sql = "select table_schema,table_name,concat(round((data_length+index_length)/1024/1024,2),'M') as size, round((data_length+index_length)/1024/1024,2) as data FROM \
        information_schema.tables where (DATA_LENGTH+INDEX_LENGTH) > {}*1024*1024*1024  and table_schema not in \
        ('information_schema','mysql','performance_schema','sys') order by size desc".format(value)
    return sql

def get_top_big_tables(limit=20):
    """
    1.3 数据量排名前 多少 的表
    :param limit:
    :return:
    """
    sql = "SELECT table_schema,table_name,concat(round((data_length + index_length)/1024/1024,2), 'M') AS all_mb,concat(round(data_length/1024/1024,2),'M') AS data_mb, \
          concat(round(index_length/1024/1024,2), 'M') AS index_mb, table_rows, round((data_length + index_length)/1024/1024,2) as count_mb FROM \
          information_schema.tables  where table_schema not in ('information_schema','mysql','performance_schema','sys') order by count_mb desc limit {}".format(limit)
    return sql

def get_table_rows(table_rows = 10000000):
    """
     1.4 单表超过行数多少万的表,默认是10000000行
     :param request
     :return:
     """
    sql = "select table_schema,table_name,table_rows from \
         information_schema.TABLES where table_schema not in ('information_schema','mysql','performance_schema','sys') \
         and table_rows > {} order by table_rows desc;".format(table_rows)
    return sql

def get_auto_increment_ratio(auto_increment_ratio = 0.3000):

    """
    1.5 自增ID占比大于 多少 的表, 默认是30%
    :param auto_increment_ratio:
    :return:
    """
    sql = "select table_schema,table_name,auto_increment_ratio,max_value,auto_increment from sys.schema_auto_increment_columns \
          where auto_increment_ratio > {} and table_schema not in \
          ('information_schema','mysql','performance_schema','sys') order by auto_increment_ratio desc".format(auto_increment_ratio)

    return sql

def get_big_fragment_tables(data_free=1):
    """
    1.6 碎片大于多少 G 的表, 默认为1G
    :param data_free:
    :return:
    """
    sql = "select table_schema,table_name,concat(round(DATA_FREE/1024/1024,2),'M') from information_schema.TABLES where table_schema not in \
          ('information_schema','mysql','performance_schema','sys') and data_free > {} *1024*1024*1024 order by DATA_FREE desc".format(data_free)
    return sql


def get_table_big_column():
    """
    1.7 统计大字段表
    :return:
    """
    sql = "select table_schema,table_name,column_name,data_type from information_schema.columns where data_type in \
          ('blob','clob','text','medium text','long text') and table_schema not in \
          ('information_schema','performance_schema','mysql','sys')"
    return sql


def get_table_long_varchar_column(character_maximum_length = 500):
    """
    1.8 统计字段类型varchar长度大于 多少 的表, 默认为 500
    :param character_maximum_length:
    :return:
    """
    sql = "select table_schema,table_name,column_name,data_type,CHARACTER_MAXIMUM_LENGTH from information_schema.columns \
        where DATA_TYPE='varchar' and CHARACTER_MAXIMUM_LENGTH > {} and table_schema not in  \
        ('information_schema','performance_schema','mysql','sys');".format(character_maximum_length)
    return sql


def get_too_much_columns_indexs(index_count = 5):
    """
    2.1 获取索引数目大于5个的表
    :param request:
    :param index_count 索引数目，默认为5
    :return:
    """
    sql = "select s.table_schema,s.table_name,s.column_name,s.index_name from information_schema.STATISTICS s, \
          (select table_name,index_name,count(*) from information_schema.STATISTICS where table_schema not in \
          ('information_schema','performance_schema','mysql','sys') group by table_name,index_name having \
          count(*)> {})t where s.table_name=t.table_name and s.index_name=t.index_name;" .format(index_count)
    return sql

def get_not_primary_index():
    """
    2.2 没有主键索引的表
    :return:
    """

    sql = "SELECT t.table_schema,t.table_name FROM information_schema.tables AS t LEFT JOIN   \
        (SELECT DISTINCT table_schema, table_name FROM information_schema.`KEY_COLUMN_USAGE` ) AS kt ON \
        kt.table_schema=t.table_schema AND kt.table_name = t.table_name WHERE t.table_schema NOT IN \
        ('mysql', 'information_schema', 'performance_schema', 'sys') AND kt.table_name IS NULL;"

    return sql


# def get_instance_user_privileges():
#     sql_get_user = '''select concat("\'", user, "\'", '@', "\'", host,"\'") as query from mysql.user;'''
#     res = get_process_data(sql_get_user, 2)
#     res_user_priv = []
#     for db_user in res:
#         user_info = {}
#         sql_get_permission = 'show grants for {};'.format(db_user[0])
#         user_priv = get_process_data(sql_get_permission, 2)
#         user_info['user'] = db_user[0]
#         user_info['privileges'] = user_priv
#         res_user_priv.append(user_info)
#     return res_user_priv


