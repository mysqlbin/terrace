# -*- coding: UTF-8 -*-
import logging
import os
import time
import traceback
import json

from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
# from django_q.tasks import async_task
from myapp.common.utils.rewrite_json_encoder import RewriteJsonEncoder
from myapp.models import Db_instance

from myapp.include.polling_project import get_table_schema_engine,get_version,get_table_size,get_top_big_tables,get_big_fragment_tables,\
    get_auto_increment_ratio,get_table_rows,get_table_big_column,get_table_long_varchar_column, get_long_transactions, get_sql_tmp_tables,\
    get_innodb_lock_waits_list,get_instance_user_privileges, get_too_much_columns_indexs,get_not_primary_index, get_param_value,get_status_value


logger = logging.getLogger('default')

def polling_list(request):

    instance_name = request.POST.get('instance_name')
    type = request.POST.get('type',)
    db_type = request.POST.get('db_type')
    limit = int(request.POST.get('limit'))
    offset = int(request.POST.get('offset'))

    instance_obj = Db_instance.objects.all()

    if instance_name != '':
        instance_obj = instance_obj.filter(instance_name__icontains=instance_name)
    if type != '':
        instance_obj = instance_obj.filter(type=type)
    if db_type != '':
        instance_obj = instance_obj.filter(db_type=db_type)

    count = instance_obj.count()
    instance_res = instance_obj[offset:limit].values('id', 'instance_name', 'type', 'db_type', 'ip', 'port', )

    # QuerySet 序列化
    rows = [row for row in instance_res]
    result = {"total": count, "rows": rows}

    return HttpResponse(json.dumps(result), content_type='application/json')


def get_polling_report(request):

    instance_id   = request.POST.get("instance_id")
    instance_name = request.POST.get("instance_name")

    try:
        insname = Db_instance.objects.get(id=int(instance_id))
    except Db_instance.DoesNotExist:
        res = {'status': 0, 'msg': '实例不存在'}
        return HttpResponse(json.dumps(res))

    timestamp = int(time.time())
    path = os.path.join(settings.BASE_DIR, 'downloads/polling/')
    filename = os.path.join(path, f"{instance_name}的巡检报告{timestamp}.sql")

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
