from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.include import meta
from myapp.include import function as func
from myapp.include import sqlfilter
from myapp.tasks import parse_to_binlog2sql
from myapp.form import AddForm
from blacklist import blFunction as bc
from myapp.models import Db_instance,SlowQuery,SlowQueryHistory

from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import F,Max,Sum,Value as V
from django.db.models.functions import Concat
from automatic import settings

from django.core import serializers

from myapp.include.polling_project import get_table_schema_engine,get_version,get_table_size,get_top_big_tables,get_big_fragment_tables,\
    get_auto_increment_ratio,get_table_rows,get_table_big_column,get_table_long_varchar_column, get_long_transactions, get_sql_tmp_tables,\
    get_innodb_lock_waits_list,get_instance_user_privileges, get_too_much_columns_indexs,get_not_primary_index, get_param_value,get_status_value


from myapp.plugins.binglog2sql import Binlog2Sql

import datetime,time
import json
import os


@login_required(login_url='/admin/login/')
def index(request):
    return render(request, 'index.html')

def get_binlog_to_sql(request):

    """
       通过解析binlog获取SQL
       :param request:
       :return:
       """

    instance = Db_instance.objects.get(id=int(1))

    # instance_name = request.POST.get('instance_name')
    save_sql = True if request.POST.get('save_sql') == 'true' else False
    # instance = Instance.objects.get(instance_name=instance_name)

    no_pk = True if request.POST.get('no_pk') == 'true' else False
    flashback = True if request.POST.get('flashback') == 'true' else False
    # back_interval = 0 if request.POST.get('back_interval') == '' else int(request.POST.get('back_interval'))
    # num = 30 if request.POST.get('num') == '' else int(request.POST.get('num'))
    back_interval = 0
    num = 30

    start_file = request.POST.get('start_file', 'mysql-bin.000006')
    start_pos = request.POST.get('start_pos') if request.POST.get('start_pos') == '' else int(request.POST.get('start_pos', 973))
    end_file = request.POST.get('end_file')
    end_pos = request.POST.get('end_pos') if request.POST.get('end_pos') == '' else int(request.POST.get('end_pos', 1208))
    stop_time = request.POST.get('stop_time', '2019-08-30 03:55:14')
    start_time = request.POST.get('start_time', '2019-08-30 03:50:14')
    only_schemas = request.POST.getlist('only_schemas')
    only_tables = request.POST.getlist('only_tables[]')
    only_dml = True if request.POST.get('only_dml') == 'true' else False
    sql_type = ['INSERT', 'UPDATE', 'DELETE'] if request.POST.getlist('sql_type[]') == [] else request.POST.getlist(
        'sql_type[]')



    # flashback=True获取DML回滚语句
    result = {'status': 0, 'msg': 'ok', 'data': ''}

    # 提交给binlog2sql进行解析

    binlog2sql = Binlog2Sql()
    # 准备参数
    args = {"conn_options": fr"-h{instance.ip} -u{instance.ip} -p'{instance.ip}' -P{instance.port} ",
           "stop_never": False,
            "no-primary-key": no_pk,
            "flashback": flashback,
            "back-interval": back_interval,
            "start-file": start_file,
            "start-position": start_pos,
            "stop-file": end_file,
            "stop-position": end_pos,
            "start-datetime": start_time,
            "stop-datetime": stop_time,
            "databases": ' '.join(only_schemas),
            "tables": ' '.join(only_tables),
            "only-dml": only_dml,
            "sql-type": ' '.join(sql_type),
            "instance": instance
    }

    # 参数检查
    args_check_result = binlog2sql.check_args(args)

    if args_check_result['status'] == 1:
        return HttpResponse(json.dumps(args_check_result), content_type='application/json')
    # 参数转换
    cmd_args = binlog2sql.generate_args2cmd(args, shell=True)
    """
    python3 binlog2sql.py -h192.168.0.54 -P3306 -uroot -p'123456abc' -ddb1 -taccountinfo --start-file='mysql-bin.000006' --start-datetime='2019-08-30 03:50:14' --stop-datetime='2019-08-30 03:55:14'
    USE b'db1';
    CREATE TABLE `accountinfo` (
      `AccountId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '账号编号',
      `Ip` varchar(512) DEFAULT NULL,
      PRIMARY KEY (`AccountId`)
    ) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
    INSERT INTO `db1`.`accountinfo`(`AccountId`, `Ip`) VALUES (1, '1'); #start 973 end 1208 time 2019-08-30 03:52:27

    python binlog2sql.py -h192.168.0.54 -u192.168.0.54 -p'192.168.0.54' -P3306 --back-interval --start-position='10' --stop-position='20' --sql-type INSERT UPDATE DELETE
    """

    # 执行命令
    try:
        p = binlog2sql.execute_cmd(cmd_args, shell=True)
        # return HttpResponse(p)
        # 读取前num行后结束
        rows = []
        n = 1
        for line in iter(p.stdout.readline, ''):
            if n <= num:
                n = n + 1
                row_info = {}
                try:
                    row_info['sql'] = line.split('; #')[0] + ";"
                    row_info['binlog_info'] = line.split('; #')[1].rstrip('\"')
                except IndexError:
                    row_info['sql'] = line
                    row_info['binlog_info'] = None
                rows.append(row_info)
            else:
                break
        if rows.__len__() == 0:
            # 判断是否有异常
            stderr = p.stderr.read()
            if stderr:
                result['status'] = 1
                result['msg'] = stderr
                return HttpResponse(json.dumps(result), content_type='application/json')
        # 终止子进程
        p.kill()
        result['data'] = rows
    except Exception as e:
        logger.error(traceback.format_exc())
        result['status'] = 1
        result['msg'] = str(e)

    # 异步保存到文件，去除conn_options避免展示密码信息
    if save_sql:
        async_task(binlog2sql_file, args=args, user=request.user, hook=notify_for_binlog2sql)

    # 返回查询结果
    return HttpResponse(json.dumps(result, cls=ExtendJSONEncoder, bigint_as_string=True),
                        content_type='application/json')

def binlog2sql(request):
    return render(request, 'binlog2sql.html')

    instance_res = instance_obj.values('id', 'instance_name', 'type', 'db_type', 'ip', 'port', )




def polling_report(request):

    type_list = {'all': '全部', 'master': '主库', 'slave': '从库', 'alone': '单机'}
    db_type_list = {'all': '全部', 'mysql': 'MySQL', 'mongodb': 'MongoDB', 'mssql': 'MsSQL', 'redis': 'Redis',
                    'pgsql': 'PgSQL', 'oracle': 'Oracle'}

    instance_name = request.POST.get('instance', 'all')
    type = request.POST.get('type', 'all')
    db_type = request.POST.get('db_type', 'all')

    instance_obj = Db_instance.objects.all()
    if instance_name != 'all':
        instance_obj = instance_obj.filter(instance_name__icontains=instance_name)
    if type != 'all':
        instance_obj = instance_obj.filter(type=type)
    if db_type != 'all':
        instance_obj = instance_obj.filter(db_type=db_type)

    instance_res = instance_obj.values('id', 'instance_name', 'type', 'db_type', 'ip', 'port', )

    return render(request, 'polling_report.html', locals())


def get_polling_report(request):

    id = request.POST.get("id")
    name = request.POST.get("name")

    try:
        insname = Db_instance.objects.get(id=int(id))
    except Db_instance.DoesNotExist:
        res = {'status': 0, 'msg': '实例不存在'}
        return HttpResponse(json.dumps(res))

    timestamp = int(time.time())
    path = os.path.join(settings.BASE_DIR, 'downloads/polling/')
    filename = os.path.join(path, f"{name}的巡检报告{timestamp}.sql")

    with open(filename, 'a+') as f:

        f.write('1.数据表巡检项:' + '\n')

        f.write('1.1 统计数据库实例存储引擎的类型的数量:' + '\n')
        schema_engine = get_table_schema_engine(insname)
        if schema_engine:
            for val in schema_engine:
                row = 'table_schema:{:15s}  engine:{:30s} engine_counts:{:15} '.format(val[0], val[1], val[2])
                f.write(row + '\n')


        table_size_custom = 1
        f.write('1.2 超过 {} G的大表:'.format(table_size_custom) + '\n')
        table_size_res = get_table_size(insname, 5)
        if table_size_res:
            for val in table_size_res:
                row = 'table_schema:{:15s}  table_name:{:30s} size:{:10s}'.format(val[0], val[1], val[2])
                f.write(row + '\n')
        else:
            f.write('###没有超过{} G的表###'.format(table_size_custom) + '\n')

        top_big_tables_custom = 20
        f.write('1.3 数据量排名前 {} 的表:'.format(top_big_tables_custom) + '\n')
        big_tables_res = get_top_big_tables(insname, top_big_tables_custom)
        if big_tables_res:
            for val in big_tables_res:
              row = 'table_schema:{:15s}  table_name:{:30s} all_size:{:15s} data_size:{:15s} index_size:{:15s} table_rows:{:5}'.format(
                    val[0], val[1], val[2], val[3], val[4], val[5])
              f.write(row + '\n')
        else:
            f.write('###没有数据量排名前 {} 的表###'.format(top_big_tables_custom) + '\n')

        table_rows_custom = 10000000
        f.write('1.4 单表超过行数 {} 表:'.format(table_rows_custom) + '\n')
        table_rows_res = get_table_rows(insname, table_rows_custom)
        if table_rows_res:
            for val in table_rows_res:
                row = 'table_schema:{:15} table_name:{:30s} table_rows:{} '.format(val[0], val[1], val[2])
                f.write(row + '\n')
        else:
            f.write('###没有单表超过行数 {} 表###'.format(table_rows_custom) + '\n')


        auto_increment_ratio_custom = 0.5000
        f.write('1.5 自增ID占比大于 {} 的表 :'.format(auto_increment_ratio_custom) + '\n')
        auto_increment_ratio_res = get_auto_increment_ratio(insname, auto_increment_ratio_custom)
        if auto_increment_ratio_res:
            for val in auto_increment_ratio_res:
                row = 'table_schema:{:15s} table_name:{:30s} auto_increment_ratio:{} max_value:{} auto_increment:{}'.format(val[0], val[1], val[2], val[3], val[4])
                f.write(row + '\n')
        else:
            f.write('###没有自增ID占比大于 {} 的表###'.format(auto_increment_ratio_custom) + '\n')

        fragment_custom = 0.0100
        f.write('1.6 碎片大于多少 {} 的表 :'.format(fragment_custom) + '\n')
        get_big_fragment_res = get_big_fragment_tables(insname, fragment_custom)
        if get_big_fragment_res:
            for val in get_big_fragment_res:
                row = 'table_schema:{:15s}  table_name:{:30s} fragment:{:10s}'. format(val[0], val[1], val[2])
                f.write(row + '\n')
        else:
            f.write('###没有碎片大于多少 {} 的表###'.format(fragment_custom) + '\n')

        f.write('1.7 统计大字段表:' + '\n')
        big_column_res = get_table_big_column(insname)
        if big_column_res:
            for val in big_column_res:
                row = 'table_schema:{:15s}  engine:{:30s} engine_counts:{:15} '.format(val[0], val[1], val[2])
                f.write(row + '\n')
        else:
            f.write('###没有大字段表###' + '\n')

        varchar_long_custom = 500
        f.write('1.8 统计字段类型varchar长度大于 {} 的表:'.format(varchar_long_custom) + '\n')
        long_varchar_res = get_table_long_varchar_column(insname, varchar_long_custom)
        if long_varchar_res:
            for val in long_varchar_res:
                row = 'table_schema:{:15} table_name:{:30s} column_name:{:30s} data_type:{:20s} CHARACTER_MAXIMUM_LENGTH:{:20}'.format(val[0], val[1], val[2], val[3], val[4])
                f.write(row + '\n')
        else:
            f.write('###统计字段类型varchar长度没有大于 {} 的表###'.format(varchar_long_custom) + '\n')


        f.write('2.索引巡检项:' + '\n')

        custom_index_counts = 5
        f.write('2.1 获取索引数目大于 {} 个的表:' .format(custom_index_counts) + '\n')
        index_counts = get_too_much_columns_indexs(insname, 5)
        if index_counts:
            for val in index_counts:
                row = 'table_schema: {:15s}  table_name: {:30s} index_name: {:20s} column_name: {:20s} '.format(val[0], val[1], val[2], val[3])
                f.write(row + '\n')
        else:
            f.write('###没有索引数目大于5的表###' .format(custom_index_counts) + '\n')


        f.write('2.2 获取没有主键索引的表:' + '\n')
        not_index_table_res = get_not_primary_index(insname)

        if not_index_table_res:
            for val in not_index_table_res:
                row = 'table_schema:{:15s}  table_name:{:30s} '.format(val[0], val[1])
                f.write(row + '\n')
        else:
            f.write('###没有主键索引的表###' + '\n')

        f.write('3.参数巡检项:' + '\n')

        f.write('3.1 InnoDB层参数:' + '\n')

        f.write('3.1.1 InnoDB层缓冲池参数:' + '\n')
        f.write(get_param_value(insname, 'innodb_random_read_ahead') + '\n')
        f.write(get_param_value(insname, 'innodb_read_ahead_threshold') + '\n')
        f.write(get_param_value(insname, 'innodb_buffer_pool_load_at_startup') + '\n')
        f.write(get_param_value(insname, 'innodb_buffer_pool_dump_at_shutdown') + '\n')
        f.write(get_param_value(insname, 'innodb_flush_neighbors') + '\n')
        f.write(get_param_value(insname, 'innodb_buffer_pool_size') + '\n')
        f.write(get_param_value(insname, 'innodb_buffer_pool_instances') + '\n')
        f.write(get_param_value(insname, 'innodb_lru_scan_depth') + '\n')
        f.write(get_param_value(insname, 'innodb_max_dirty_pages_pct') + '\n')
        f.write(get_param_value(insname, 'innodb_old_blocks_pct') + '\n')
        f.write(get_param_value(insname, 'innodb_old_blocks_time') + '\n')

        f.write('3.1.2 InnoDB层redo参数:' + '\n')
        f.write(get_param_value(insname, 'innodb_flush_log_at_trx_commit') + '\n')
        f.write(get_param_value(insname, 'innodb_log_file_size') + '\n')
        f.write(get_param_value(insname, 'innodb_log_files_in_group') + '\n')
        f.write(get_param_value(insname, 'innodb_log_buffer_size') + '\n')

        f.write('3.1.3 InnoDB层持久化统计信息参数:' + '\n')
        f.write(get_param_value(insname, 'innodb_stats_persistent') + '\n')
        f.write(get_param_value(insname, 'innodb_stats_persistent_sample_pages') + '\n')
        f.write(get_param_value(insname, 'innodb_stats_auto_recalc') + '\n')

        f.write('3.1.4 InnoDB层其它参数:' + '\n')
        f.write(get_param_value(insname, 'innodb_rollback_on_timeout') + '\n')
        f.write(get_param_value(insname, 'innodb_io_capacity') + '\n')
        f.write(get_param_value(insname, 'innodb_io_capacity_max') + '\n')
        f.write(get_param_value(insname, 'innodb_autoinc_lock_mode') + '\n')
        f.write(get_param_value(insname, 'innodb_flush_method') + '\n')
        f.write(get_param_value(insname, 'innodb_file_per_table') + '\n')
        f.write(get_param_value(insname, 'innodb_open_files') + '\n')
        f.write(get_param_value(insname, 'innodb_data_home_dir') + '\n')
        f.write(get_param_value(insname, 'innodb_lock_wait_timeout') + '\n')
        f.write(get_param_value(insname, 'innodb_thread_concurrency') + '\n')
        f.write(get_param_value(insname, 'innodb_fast_shutdown') + '\n')
        f.write(get_param_value(insname, 'innodb_rollback_on_timeout') + '\n')
        f.write(get_param_value(insname, 'innodb_data_file_path') + '\n')
        f.write(get_param_value(insname, 'innodb_write_io_threads') + '\n')
        f.write(get_param_value(insname, 'innodb_read_io_threads') + '\n')
        f.write(get_param_value(insname, 'innodb_purge_threads') + '\n')
        f.write(get_param_value(insname, 'innodb_page_cleaners') + '\n')
        f.write(get_param_value(insname, 'innodb_doublewrite') + '\n')
        f.write(get_param_value(insname, 'innodb_change_buffer_max_size') + '\n')
        f.write(get_param_value(insname, 'innodb_change_buffering') + '\n')
        f.write(get_param_value(insname, 'innodb_adaptive_hash_index') + '\n')

        f.write('3.2 Server层参数:' + '\n')
        f.write('3.2.1 Server层binlog参数:' + '\n')
        f.write(get_param_value(insname, 'sync_binlog') + '\n')
        f.write(get_param_value(insname, 'binlog_format') + '\n')
        f.write(get_param_value(insname, 'binlog_row_image') + '\n')
        f.write(get_param_value(insname, 'max_binlog_size') + '\n')
        f.write(get_param_value(insname, 'max_binlog_cache_size') + '\n')
        f.write(get_param_value(insname, 'expire_logs_days') + '\n')
        f.write(get_param_value(insname, 'binlog_cache_size') + '\n')
        f.write(get_param_value(insname, 'binlog_group_commit_sync_delay') + '\n')
        f.write(get_param_value(insname, 'binlog_group_commit_sync_no_delay_count') + '\n')
        f.write(get_param_value(insname, 'binlog_transaction_dependency_tracking') + '\n')

        f.write('3.2.2 Server层线程/会话相关的内存参数:' + '\n')
        f.write(get_param_value(insname, 'key_buffer_size') + '\n')
        f.write(get_param_value(insname, 'query_cache_size') + '\n')
        f.write(get_param_value(insname, 'read_buffer_size') + '\n')
        f.write(get_param_value(insname, 'read_rnd_buffer_size') + '\n')
        f.write(get_param_value(insname, 'sort_buffer_size') + '\n')
        f.write(get_param_value(insname, 'join_buffer_size') + '\n')
        f.write(get_param_value(insname, 'tmp_table_size') + '\n')

        f.write('3.2.3 Server层其它参数:' + '\n')
        f.write(get_param_value(insname, 'max_allowed_packet') + '\n')
        f.write(get_param_value(insname, 'net_buffer_length') + '\n')
        f.write(get_param_value(insname, 'table_open_cache') + '\n')
        f.write(get_param_value(insname, 'max_execution_time') + '\n')
        f.write(get_param_value(insname, 'sql_mode') + '\n')
        f.write(get_param_value(insname, 'interactive_timeout') + '\n')
        f.write(get_param_value(insname, 'wait_timeout') + '\n')
        f.write(get_param_value(insname, 'open_files_limit') + '\n')
        f.write(get_param_value(insname, 'lower_case_table_names') + '\n')
        f.write(get_param_value(insname, 'slow_query_log') + '\n')
        f.write(get_param_value(insname, 'long_query_time') + '\n')
        f.write(get_param_value(insname, 'log_queries_not_using_indexes') + '\n')
        f.write(get_param_value(insname, 'system_time_zone') + '\n')
        f.write(get_param_value(insname, 'time_zone') + '\n')
        f.write(get_param_value(insname, 'log_timestamps') + '\n')
        f.write(get_param_value(insname, 'max_connections') + '\n')
        f.write(get_param_value(insname, 'max_connect_errors') + '\n')
        f.write(get_param_value(insname, 'max_user_connections') + '\n')
        # f.write(get_status_value(insname, 'Max_used_connections') + '\n')

        f.write('4. 状态巡检项:' + '\n')
        f.write('4.1 InnoDB层缓冲池状态值:' + '\n')
        f.write(get_status_value(insname, 'innodb_buffer_pool_pages_dirty') + '\n')
        f.write(get_status_value(insname, 'innodb_buffer_pool_pages_total') + '\n')
        f.write(get_status_value(insname, 'Innodb_buffer_pool_pages_data') + '\n')
        f.write(get_status_value(insname, 'Innodb_buffer_pool_pages_flushed') + '\n')
        f.write(get_status_value(insname, 'innodb_buffer_pool_read_requests') + '\n')
        f.write(get_status_value(insname, 'innodb_buffer_pool_read_ahead') + '\n')
        f.write(get_status_value(insname, 'Innodb_buffer_pool_read_ahead_evicted') + '\n')
        f.write(get_status_value(insname, 'innodb_buffer_pool_reads') + '\n')
        f.write(get_status_value(insname, 'Innodb_buffer_pool_pages_free') + '\n')
        f.write(get_status_value(insname, 'Innodb_buffer_pool_wait_free') + '\n')

        ibp_pages_dirty = get_status_value(insname, 'innodb_buffer_pool_pages_dirty', 0)
        ibp_pages_total = get_status_value(insname, 'innodb_buffer_pool_pages_total', 0)
        dirty_page = round(int(ibp_pages_dirty) / int(ibp_pages_total), 4)
        f.write('脏页在缓冲池数据页中的占比为: {}%'.format(dirty_page * 100) + '\n')

        ibp_read_requests = get_status_value(insname, 'innodb_buffer_pool_read_requests', 0)
        ibp_read_ahead    = get_status_value(insname, 'innodb_buffer_pool_read_ahead', 0)
        ibp_read_reads    = get_status_value(insname, 'innodb_buffer_pool_reads', 0)
        ibp_hit = round(int(ibp_read_requests) / (int(ibp_read_requests) + int(ibp_read_ahead) + int(ibp_read_reads)), 4)
        f.write('InnoDB buffer pool 命中率: {}%'.format(ibp_hit * 100) + '\n')

        ibp_wait_free = get_status_value(insname, 'Innodb_buffer_pool_wait_free', 0)
        if int(ibp_wait_free) > 0:
            f.write('注意：InnoDB Buffer Pool可能不够用了，需要详细检查并处理，目前等待申请空闲列表的次数为: {} 次'.format(ibp_wait_free) + '\n')

        f.write('4.2 并发线程连接数:' + '\n')
        f.write(get_status_value(insname, 'Threads_connected') + '\n')
        f.write(get_status_value(insname, 'Threads_created') + '\n')
        f.write(get_status_value(insname, 'Threads_running') + '\n')

        f.write('4.3 InnoDB行锁等待:' + '\n')
        f.write(get_status_value(insname, 'Innodb_row_lock_current_waits') + '\n')
        f.write(get_status_value(insname, 'Innodb_row_lock_time') + '\n')
        f.write(get_status_value(insname, 'Innodb_row_lock_time_avg') + '\n')
        f.write(get_status_value(insname, 'Innodb_row_lock_time_max') + '\n')
        f.write(get_status_value(insname, 'Innodb_row_lock_waits') + '\n')

        f.write('4.4 打开表的次数:' + '\n')
        f.write(get_status_value(insname, 'Open_files') + '\n')
        f.write(get_status_value(insname, 'Open_tables') + '\n')
        f.write(get_status_value(insname, 'Opened_tables') + '\n')

        f.write('4.5 创建内存临时表和磁盘临时表的次数:' + '\n')
        f.write(get_status_value(insname, 'Created_tmp_tables') + '\n')
        f.write(get_status_value(insname, 'Created_tmp_disk_tables') + '\n')

        f.write('4.6 InnoDB关键特性double write的使用情况:' + '\n')
        f.write(get_status_value(insname, 'Innodb_dblwr_pages_written') + '\n')
        f.write(get_status_value(insname, 'Innodb_dblwr_writes') + '\n')
        dblwr_pages_written = get_status_value(insname, 'Innodb_dblwr_pages_written', 0)
        dblwr_writes = get_status_value(insname, 'Innodb_dblwr_writes', 0)
        merge_pages = int(dblwr_pages_written) / int(dblwr_writes)
        f.write('每次写操作合并page的个数: {}'.format((round(merge_pages, 0))) + '\n')

        f.write('4.7 因log buffer不足导致等待的次数:' + '\n')
        f.write(get_status_value(insname, 'Innodb_log_waits') + '\n')
        innodb_log_waits = get_status_value(insname, 'Innodb_log_waits', 0)
        if int(innodb_log_waits) > 0:
            f.write('注意：因 log buffer不足导致等待的次数(Innodb_log_waits): {} 次'.format(ibp_wait_free) + '\n')


        f.write('5. 其它巡检项:' + '\n')

        sql_counts_custom = 20
        f.write('5.1 使用到内存临时表或者磁盘临时表的前 {} 个SQL:'.format(sql_counts_custom) + '\n')
        sql_tmp_tables_res = get_sql_tmp_tables(insname, sql_counts_custom)
        if sql_tmp_tables_res:
            for val in sql_tmp_tables_res:
                if val[0] != None:
                    db_name = val[0]
                    row =  'db_name:{:20s} tmp_tables:{} tmp_disk_tables:{} tmp_all:{} last_seen:{} query_sql:{}'.format(db_name, val[1], val[2], val[3], val[4], val[5])
                    f.write(row + '\n')
        else:
            f.write('没有使用到内存临时表或者磁盘临时表的前 {} 个SQL:'.format(sql_counts_custom) + '\n')


        long_transactions_time_custom = 1
        f.write('5.2 获取执行时间大于 {} 秒的长事务:'.format(long_transactions_time_custom) + '\n')
        long_transactionss_res = get_long_transactions(insname, long_transactions_time_custom)
        if long_transactionss_res:
            for val in long_transactionss_res:
                if val[8] == None:
                    trx_query = ''
                else:
                    trx_query = val[0]
                row = 'host:{:20s} user:{:20s} db:{:20s} trx_state:{:10s} command:{:10s} time:{:10s} trx_id:{:10s} thread_id:{}  trx_query:{:20s} '.format(
                    val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], trx_query)
                f.write(row + '\n')

        else:
            f.write('没有执行时间大于 {} 秒的长事务:'.format(long_transactions_time_custom) + '\n')

        f.write('5.3 行锁等待列表:' + '\n')
        lock_wait_res = get_innodb_lock_waits_list(insname)
        if lock_wait_res:
            for val in lock_wait_res:
                row = 'locked_index:{:10s} locked_type:{:10s} blocking_block_mode:{:10s} waiting_lock_mode:{:10s} waiting_query:{}'.format(
                    val[0], val[1], val[2], val[3], val[4])
                f.write(row + '\n')
        else:
            f.write('没有行锁等待' + '\n')

        res = {'status': 1, 'msg': '数据库巡检报告已经下载到项目的downloads文件夹下'}

        return HttpResponse(json.dumps(res))

def instance(request):

    type_list = {'all': '全部', 'master': '主库', 'slave': '从库', 'alone': '单机'}
    db_type_list = {'all': '全部', 'mysql': 'MySQL', 'mongodb': 'MongoDB', 'mssql': 'MsSQL', 'redis': 'Redis', 'pgsql': 'PgSQL', 'oracle': 'Oracle'}

    instance_name = request.POST.get('instance', 'all')
    type          = request.POST.get('type', 'all')
    db_type       = request.POST.get('db_type', 'all')

    instance_obj = Db_instance.objects.all()
    if instance_name != 'all':
        instance_obj = instance_obj.filter(instance_name__icontains=instance_name)
    if type != 'all':
        instance_obj = instance_obj.filter(type=type)
    if db_type != 'all':
        instance_obj = instance_obj.filter(db_type=db_type)

    instance_res = instance_obj.values('id', 'instance_name', 'type', 'db_type', 'ip', 'port', )

    return render(request, 'instance.html', locals())


def ins_users(request, id, instance_name):

    instance_name = instance_name
    try:
        insname = Db_instance.objects.get(id=int(id))
    except Db_instance.DoesNotExist:
       return HttpResponse('实例不存在')

    sql_get_user = '''select concat("\'", user, "\'", '@', "\'", host,"\'") as query from mysql.user;'''
    users_res, col = meta.get_process_data(insname, sql_get_user)
    # return HttpResponse(col)
    # 获取用户权限信息
    res_user_priv = []
    for db_user in users_res:
        user_info = {}
        sql_get_permission        = 'show grants for {};'.format(db_user[0])
        user_priv, col            = meta.get_process_data(insname, sql_get_permission)
        user_info['user']        = db_user[0]
        user_info['privileges'] = user_priv
        res_user_priv.append(user_info)

    return render(request, 'users.html', locals())


def slow_query(request):

    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
    insname = Db_instance.objects.get(id=int(request.POST.get('instance', '3')))
    dbname_res = insname.db_name_set.all().values('dbname')

    dblist = []
    if dbname_res.exists():
        dblist.append('全部数据库')
        for res in dbname_res:
            dblist.append(res.get('dbname'))

    db_name = request.POST.get('dbname')

    default_begin_time = time.strftime("%Y-%m-%d")
    default_begin_time = datetime.datetime.strptime(default_begin_time, '%Y-%m-%d') + datetime.timedelta(days=-1)

    default_stop_time  = time.strftime('%Y-%m-%d %X', time.localtime())
    default_range_time = '{} To {}'.format(default_begin_time, default_stop_time)
    range_time = request.POST.get('range-time', default_range_time)
    range_time_split = range_time.split("To")

    start_time = range_time_split[0].strip()
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')

    end_time = range_time_split[1].strip()
    end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    if db_name and db_name != '全部数据库':
        # 获取慢查数据, 跨表多对一查询
        slowsql_obj = SlowQuery.objects.filter(
            slowqueryhistory__hostname_max=('{}:{}'.format(insname.ip, insname.port)),
            slowqueryhistory__db_max=db_name,
            slowqueryhistory__ts_min__range=(start_time, end_time)
        ).annotate(SQLText=F('fingerprint'), SQLId=F('checksum')).values('SQLText', 'SQLId').annotate(
            CreateTime=Max('slowqueryhistory__ts_max'),
            DBName=Max('slowqueryhistory__db_max'),  # 数据库
            QueryTimeAvg=Sum('slowqueryhistory__query_time_sum') / Sum('slowqueryhistory__ts_cnt'),  # 平均执行时长
            MySQLTotalExecutionCounts=Sum('slowqueryhistory__ts_cnt'),  # 执行总次数
            MySQLTotalExecutionTimes=Sum('slowqueryhistory__query_time_sum'),  # 执行总时长
            ParseTotalRowCounts=Sum('slowqueryhistory__rows_examined_sum'),  # 扫描总行数
            ReturnTotalRowCounts=Sum('slowqueryhistory__rows_sent_sum'),  # 返回总行数
        )
    else:
        # 获取慢查数据, 跨表多对一查询
        slowsql_obj = SlowQuery.objects.filter(
            slowqueryhistory__hostname_max=('{}:{}'.format(insname.ip, insname.port)),
            slowqueryhistory__ts_min__range=(start_time, end_time),
        ).annotate(SQLText=F('fingerprint'), SQLId=F('checksum')).values('SQLText', 'SQLId').annotate(
            CreateTime=Max('slowqueryhistory__ts_max'),
            DBName=Max('slowqueryhistory__db_max'),  # 数据库
            QueryTimeAvg=Sum('slowqueryhistory__query_time_sum') / Sum('slowqueryhistory__ts_cnt'),  # 平均执行时长
            MySQLTotalExecutionCounts=Sum('slowqueryhistory__ts_cnt'),  # 执行总次数
            MySQLTotalExecutionTimes=Sum('slowqueryhistory__query_time_sum'),  # 执行总时长
            ParseTotalRowCounts=Sum('slowqueryhistory__rows_examined_sum'),  # 扫描总行数
            ReturnTotalRowCounts=Sum('slowqueryhistory__rows_sent_sum'),  # 返回总行数
        )

    slow_sql_result = slowsql_obj.order_by('-MySQLTotalExecutionCounts')

    return render(request, 'show_query.html', locals())


def slowquery_review_history(request, SQLId, startTime, endTime):

    hostname_db_max_results = SlowQueryHistory.objects.filter(checksum=SQLId).values('hostname_max', 'db_max')[0:1]

    ip_addr = '127.0.0.1'
    port = 3306
    has_db_name = ''
    if hostname_db_max_results.exists():
        hostname_max = ''
        for res in hostname_db_max_results:
            hostname_max = res.get('hostname_max')
            has_db_name  = res.get('db_max')
        hostname_max_list = hostname_max.split(":")
        ip_addr = hostname_max_list[0]
        port = hostname_max_list[1]

    instance_res = Db_instance.objects.get(ip=ip_addr, port=port)
    dbname_res = instance_res.db_name_set.all().values('dbname')

    dblist = []
    if dbname_res.exists():
        dblist.append('全部数据库')
        for res in dbname_res:
            dblist.append(res.get('dbname'))

    sql_id = ''
    db_name = request.POST.get('dbname', has_db_name)
    if db_name == '' and has_db_name == '':
        sql_id = '{}'.format(SQLId)

    default_begin_time = startTime
    default_stop_time = endTime
    default_range_time = '{} To {}'.format(default_begin_time, default_stop_time)

    range_time = request.POST.get('range-time', default_range_time)
    range_time_split = range_time.split("To")

    start_time = range_time_split[0].strip()
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = range_time_split[1].strip()
    end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    if sql_id:
        # 获取慢查明细数据
        slow_sql_record_result = SlowQueryHistory.objects.filter(
            hostname_max=('{}:{}'.format(instance_res.ip, instance_res.port)),
            checksum=sql_id,
            ts_min__range=(start_time, end_time)
        ).annotate(ExecutionStartTime=F('ts_min'),  # 本次统计(每5分钟一次)该类型sql语句出现的最小时间
                   DBName=F('db_max'),  # 数据库名
                   HostAddress=Concat(V('\''), 'user_max', V('\''), V('@'), V('\''), 'client_max', V('\'')),  # 用户名
                   SQLText=F('sample'),  # SQL语句
                   TotalExecutionCounts=F('ts_cnt'),  # 本次统计该sql语句出现的次数
                   QueryTimePct95=F('query_time_pct_95'),  # 本次统计该sql语句95%耗时
                   QueryTimes=F('query_time_sum'),  # 本次统计该sql语句花费的总时间(秒)
                   LockTimes=F('lock_time_sum'),  # 本次统计该sql语句锁定总时长(秒)
                   ParseRowCounts=F('rows_examined_sum'),  # 本次统计该sql语句解析总行数
                   ReturnRowCounts=F('rows_sent_sum')  # 本次统计该sql语句返回总行数
                   )
    else:
        if db_name and db_name != '全部数据库':
            # 获取慢查明细数据
            slow_sql_record_result = SlowQueryHistory.objects.filter(
                hostname_max=('{}:{}'.format(instance_res.ip, instance_res.port)),
                db_max=db_name,
                ts_min__range=(start_time, end_time)
            ).annotate(ExecutionStartTime=F('ts_min'),  # 本次统计(每5分钟一次)该类型sql语句出现的最小时间
                       DBName=F('db_max'),  # 数据库名
                       HostAddress=Concat(V('\''), 'user_max', V('\''), V('@'), V('\''), 'client_max', V('\'')), # 用户名
                       SQLText=F('sample'),  # SQL语句
                       TotalExecutionCounts=F('ts_cnt'),  # 本次统计该sql语句出现的次数
                       QueryTimePct95=F('query_time_pct_95'),  # 本次统计该sql语句出现的次数
                       QueryTimes=F('query_time_sum'),  # 本次统计该sql语句花费的总时间(秒)
                       LockTimes=F('lock_time_sum'),  # 本次统计该sql语句锁定总时长(秒)
                       ParseRowCounts=F('rows_examined_sum'),  # 本次统计该sql语句解析总行数
                       ReturnRowCounts=F('rows_sent_sum')  # 本次统计该sql语句返回总行数
                       )
        else:
            # 获取慢查明细数据
            slow_sql_record_result = SlowQueryHistory.objects.filter(
                hostname_max=('{}:{}'.format(instance_res.ip, instance_res.port)),
                ts_min__range=(start_time, end_time)
            ).annotate(ExecutionStartTime=F('ts_min'),  # 本次统计(每5分钟一次)该类型sql语句出现的最小时间
                       DBName=F('db_max'),  # 数据库名
                       HostAddress=Concat(V('\''), 'user_max', V('\''), V('@'), V('\''), 'client_max', V('\'')), # 用户名
                       SQLText=F('sample'),  # SQL语句
                       TotalExecutionCounts=F('ts_cnt'),  # 本次统计该sql语句出现的次数
                       QueryTimePct95=F('query_time_pct_95'),  # 本次统计该sql语句95%耗时
                       QueryTimes=F('query_time_sum'),  # 本次统计该sql语句花费的总时间(秒)
                       LockTimes=F('lock_time_sum'),  # 本次统计该sql语句锁定总时长(秒)
                       ParseRowCounts=F('rows_examined_sum'),  # 本次统计该sql语句解析总行数
                       ReturnRowCounts=F('rows_sent_sum')  # 本次统计该sql语句返回总行数
                       )

        slow_sql_record_result = slow_sql_record_result.values('ExecutionStartTime',
                                                               'DBName',
                                                               'HostAddress',
                                                               'SQLText',
                                                               'TotalExecutionCounts',
                                                               'QueryTimePct95',
                                                               'QueryTimes',
                                                               'LockTimes',
                                                               'ParseRowCounts',
                                                               'ReturnRowCounts')

    return render(request, 'showsql_info.html', locals())





def get_all_instances(request):

    instance_obj = Db_instance.objects.values('instance_name', 'id')
    rows = [row for row in instance_obj]
    res = {'status': 1, 'msg': 'ok', 'data': rows}
    return HttpResponse(json.dumps(res))

def get_instances_resource(request):

    resource_type = request.POST.get('resource_type')
    db_name = request.POST.get('db_name')
    schema_name = request.POST.get('schema_name')
    tb_name = request.POST.get('tb_name')

    insname = Db_instance.objects.get(id = int(request.POST.get('data_id')))

    result = {'status': 1, 'msg': 'ok', 'data': []}

    # insname = Db_instance.objects.get(id=int(1))
    # db_name = 'db1'

    if resource_type == 'database':
        dbresult, col = meta.get_process_data(insname, 'show databases')
        resource = [row[0] for row in dbresult
                   if row[0] not in ('information_schema', 'performance_schema', 'mysql', 'test', 'sys')]

    elif resource_type == 'table':
        dbtable, col = meta.get_process_data(insname, 'show tables', db_name)
        resource = [row[0] for row in dbtable if row[0] not in ['test']]

    result['data'] = resource

    return HttpResponse(json.dumps(result), content_type = 'application/json')


def get_instances_binlog(request):

    result = {'status': 1, 'msg': 'ok', 'data': []}
    insname = Db_instance.objects.get(id=int(request.POST.get('data_id')))
    binlog, col = meta.get_process_data(insname, 'show binary logs')
    resource = [row for row in binlog]
    result['data'] = resource

    return HttpResponse(json.dumps(result), content_type='application/json')

@login_required(login_url='/admin/login/')
def binlog_parse(request):

    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
    if request.method == 'POST':
        try:

            parse_sql_number = settings.parse_sql_number

            insname = Db_instance.objects.get(id=int(request.POST['ins_set']))
            binresult, col = meta.get_process_data(insname, 'show binary logs')
            dbresult, col = meta.get_process_data(insname, 'show databases')
            binlist = []
            dblist = []
            if col != ['error']:
                dblist.append('all')
                for i in binresult:
                    binlist.append(i[0])
                for i in dbresult:
                    dblist.append(i[0])
            else:
                del binlist
                return render(request, 'binlog_parse.html', locals())

            if 'show_binary' in request.POST:
                return render(request, 'binlog_parse.html', locals())

            elif 'parse_commit' in request.POST:
                binname    = request.POST['binary']
                start_pos  = request.POST['start_pos']
                stop_pos   = request.POST['stop_pos']
                begin_time = request.POST['begin_time']
                stop_time  = request.POST['stop_time']
                tbname     = request.POST['tbname']
                dbname     = request.POST['dbname']
                sql_type   = int(request.POST['sql_type'])
                countnum   = int(request.POST['countnum'])

                start_pos = None if not start_pos else int(start_pos)
                stop_pos  = None if not stop_pos else int(stop_pos)

                if dbname == 'all':
                    dbname = None

                flashback = True if sql_type == 1 else False
                
                sqllist = parse_to_binlog2sql(insname, binname, start_pos, stop_pos, begin_time, stop_time, dbname, tbname, flashback, countnum)
                return render(request, 'binlog_parse.html', locals())

        except Exception as e:

            return render(request, 'binlog_parse.html', locals())
    else:
        return render(request, 'binlog_parse.html', locals())



def mysql_querys(request):

    objlist = func.get_mysql_hostlist('binbin')

    choosed_host = 'tags'

    a = 'select * from myapp_db_account'

    try:
        # print func.sql_init_filter(a)
        a = sqlfilter.get_sql_detail(sqlfilter.sql_init_filter(a), 1)[0]
    except Exception as e:
        a = 'wrong'
        pass

    advice = func.get_advice(choosed_host, a, request)
    return HttpResponse(advice)

# def mysql_querys(request):
#     #print request.user.username
#     # print request.user.has_perm('myapp.can_mysql_query')
#
#     objlist = func.get_mysql_hostlist('binbin')
#
#     choosed_host = 'tags'
#
#     a = 'select * from myapp_db_account'
#
#     # get first valid statement
#     try:
#         #print func.sql_init_filter(a)
#         a = sqlfilter.get_sql_detail(sqlfilter.sql_init_filter(a), 1)[0]
#     except Exception as e:
#         a='wrong'
#         pass
#
#     #return HttpResponse(a)
#
#
#     a,numlimit = func.check_mysql_query(a,'binbin')
#     return HttpResponse(a)
#     (data_list) = func.get_mysql_data(choosed_host,a,'binbin',request,numlimit)
#     return HttpResponse(data_list)
#     if a == func.wrong_msg:
#         del a
#         # print choosed_host
#         #return HttpResponse(locals)
#         #return render(request, 'mysql_query.html', locals())
#     #return HttpResponse(locals)

def mysql_query(request):
    #print request.user.username
    # print request.user.has_perm('myapp.can_mysql_query')
    try:
        favword = request.COOKIES['myfavword']
    except Exception as e:
        pass
    objlist = func.get_mysql_hostlist('binbin')
    if request.method == 'POST':
        form = AddForm(request.POST)
        # request.session['myfavword'] = request.POST['favword']
        choosed_host = request.POST['cx']

        # if not User.objects.get(username='binbin').db_name_set.filter(dbtag=choosed_host)[:1]:
        #     return HttpResponseRedirect("/")

        if 'searchdb' in request.POST:
            db_se = request.POST['searchdbname']
            objlist_tmp = func.get_mysql_hostlist('binbin', 'tag', db_se)
            # incase not found any db
            if len(objlist_tmp) > 0:
                objlist = objlist_tmp

        if form.is_valid():
            a = form.cleaned_data['a']
            # get first valid statement
            try:
                #print func.sql_init_filter(a)
                a = sqlfilter.get_sql_detail(sqlfilter.sql_init_filter(a), 1)[0]
            except Exception as e:
                a='wrong'
                pass
            try:
                #show explain
                if 'explain' in request.POST:
                    a = func.check_explain (a)
                    (data_list,collist,dbname) = func.get_mysql_data(choosed_host,a,'binbin',request,100)
                    return render(request, 'mysql_query.html', locals())
                    # return render(request,'mysql_query.html',{'form': form,'objlist':objlist,'data_list':data_list,'collist':collist,'choosed_host':choosed_host,'dbname':dbname})
                    #export csv
                elif 'query' in request.POST:
                    #check if table in black list and if user has permit to query
                    inBlackList,blacktb = bc.Sqlparse(a).check_query_table(choosed_host,'binbin')
                    if inBlackList:
                        return render(request, 'mysql_query.html', locals())
                    #get nomal query
                    a,numlimit = func.check_mysql_query(a,'binbin')
                    (data_list,collist,dbname) = func.get_mysql_data(choosed_host,a,'binbin',request,numlimit)
                    # donot show wrong message sql
                    if a == func.wrong_msg:
                        del a
                    # print choosed_host
                    return render(request, 'mysql_query.html', locals())
                elif 'sqladvice' in request.POST:

                    advice = func.get_advice(choosed_host, a, request)
                    return render(request, 'mysql_query.html', locals())

                return render(request, 'mysql_query.html', locals())

            except Exception as e:
                print(e)
                return render(request, 'mysql_query.html', locals())

        else:
            return render(request, 'mysql_query.html', locals())
            # return render(request, 'mysql_query.html', {'form': form,'objlist':objlist})
    else:
        form = AddForm()
        return render(request, 'mysql_query.html', locals())
        # return render(request, 'mysql_query.html', {'form': form,'objlist':objlist})

