1.数据表巡检项:
1.1 统计数据库实例存储引擎的类型的数量:
table_schema:dt_query         engine:InnoDB                         engine_counts:              3 
table_schema:dt_query         engine:MyISAM                         engine_counts:              8 
table_schema:repl_monitor     engine:InnoDB                         engine_counts:              2 
table_schema:sbtest           engine:InnoDB                         engine_counts:             10 
table_schema:terrace_db       engine:InnoDB                         engine_counts:             24 
table_schema:zst              engine:InnoDB                         engine_counts:              6 
1.2 超过 1 G的大表:
###没有超过1 G的表###
1.3 数据量排名前 20 的表:
table_schema:dt_query         table_name:cron_result                    all_size:8.52M           data_size:0.00M           index_size:8.52M           table_rows:288792
table_schema:dt_query         table_name:tamzsaleranks                  all_size:627.02M         data_size:161.62M         index_size:788.64M         table_rows:4095592
table_schema:sbtest           table_name:sbtest8                        all_size:54.58M          data_size:4.50M           index_size:59.08M          table_rows:196982
table_schema:sbtest           table_name:sbtest2                        all_size:54.58M          data_size:4.48M           index_size:59.06M          table_rows:172682
table_schema:sbtest           table_name:sbtest7                        all_size:53.58M          data_size:4.52M           index_size:58.09M          table_rows:169987
table_schema:sbtest           table_name:sbtest6                        all_size:53.58M          data_size:4.52M           index_size:58.09M          table_rows:184937
table_schema:sbtest           table_name:sbtest4                        all_size:53.58M          data_size:4.52M           index_size:58.09M          table_rows:189339
table_schema:sbtest           table_name:sbtest9                        all_size:53.58M          data_size:4.52M           index_size:58.09M          table_rows:178798
table_schema:sbtest           table_name:sbtest3                        all_size:53.58M          data_size:4.50M           index_size:58.08M          table_rows:179437
table_schema:sbtest           table_name:sbtest10                       all_size:53.58M          data_size:4.50M           index_size:58.08M          table_rows:176353
table_schema:sbtest           table_name:sbtest1                        all_size:52.58M          data_size:4.52M           index_size:57.09M          table_rows:177128
table_schema:sbtest           table_name:sbtest5                        all_size:52.58M          data_size:4.50M           index_size:57.08M          table_rows:183016
table_schema:dt_query         table_name:cron_origin                    all_size:27.55M          data_size:0.00M           index_size:27.55M          table_rows:975246
table_schema:zst              table_name:t1_1yi                         all_size:2218.00M        data_size:0.00M           index_size:2218.00M        table_rows:95674500
table_schema:zst              table_name:t1_10yi                        all_size:1309.00M        data_size:0.00M           index_size:1309.00M        table_rows:56484099
table_schema:dt_query         table_name:tamz_sale_ranks                all_size:811.00M         data_size:251.55M         index_size:1062.55M        table_rows:4014141
table_schema:terrace_db       table_name:myapp_user_profile             all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    0
table_schema:terrace_db       table_name:myapp_oper_log                 all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    0
table_schema:terrace_db       table_name:django_admin_log               all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:   32
table_schema:terrace_db       table_name:myapp_db_name_instance         all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    6
1.4 单表超过行数 10000000 表:
table_schema:zst             table_name:t1_1yi                         table_rows:95674500 
table_schema:zst             table_name:t1_10yi                        table_rows:56484099 
1.5 自增ID占比大于 0.5 的表 :
###没有自增ID占比大于 0.5 的表###
1.6 碎片大于多少 0.01 的表 :
###没有碎片大于多少 0.01 的表###
1.7 统计大字段表:
table_schema:repl_monitor     engine:slave_statment                 engine_counts:last_sql_error  
table_schema:repl_monitor     engine:slave_statment                 engine_counts:slave_sql_running_state 
1.8 统计字段类型varchar长度大于 500 的表:
table_schema:dt_query        table_name:tamz_sale_ranks                column_name:FItemName                      data_type:varchar              CHARACTER_MAXIMUM_LENGTH:                2048
table_schema:dt_query        table_name:tamzsaleranks                  column_name:FItemName                      data_type:varchar              CHARACTER_MAXIMUM_LENGTH:                2048
2.索引巡检项:
2.1 获取索引数目大于 5 个的表:
###没有索引数目大于5的表###
2.2 获取没有主键索引的表:
###没有主键索引的表###
3.参数巡检项:
3.1 InnoDB层参数:
3.1.1 InnoDB层缓冲池参数:
innodb_random_read_ahead : OFF
innodb_read_ahead_threshold : 56
innodb_buffer_pool_load_at_startup : ON
innodb_buffer_pool_dump_at_shutdown : ON
innodb_flush_neighbors : 1
innodb_buffer_pool_size : 104857600
innodb_buffer_pool_instances : 1
innodb_lru_scan_depth : 1024
innodb_max_dirty_pages_pct : 50.000000
innodb_old_blocks_pct : 37
innodb_old_blocks_time : 1000
3.1.2 InnoDB层redo参数:
innodb_flush_log_at_trx_commit : 2
innodb_log_file_size : 104857600
innodb_log_files_in_group : 3
innodb_log_buffer_size : 8388608
3.1.3 InnoDB层持久化统计信息参数:
innodb_stats_persistent : ON
innodb_stats_persistent_sample_pages : 20
innodb_stats_auto_recalc : ON
3.1.4 InnoDB层其它参数:
innodb_rollback_on_timeout : ON
innodb_io_capacity : 2000
innodb_io_capacity_max : 4000
innodb_autoinc_lock_mode : 1
innodb_flush_method : O_DIRECT
innodb_file_per_table : ON
innodb_open_files : 2048
innodb_data_home_dir : 
innodb_lock_wait_timeout : 50
innodb_thread_concurrency : 0
innodb_fast_shutdown : 1
innodb_rollback_on_timeout : ON
innodb_data_file_path : ibdata1:100M:autoextend
innodb_write_io_threads : 4
innodb_read_io_threads : 4
innodb_purge_threads : 4
innodb_page_cleaners : 1
innodb_doublewrite : ON
innodb_change_buffer_max_size : 25
innodb_change_buffering : all
innodb_adaptive_hash_index : ON
3.2 Server层参数:
3.2.1 Server层binlog参数:
sync_binlog : 0
binlog_format : ROW
binlog_row_image : FULL
max_binlog_size : 268435456
max_binlog_cache_size : 18446744073709547520
expire_logs_days : 10
binlog_cache_size : 32768
binlog_group_commit_sync_delay : 0
binlog_group_commit_sync_no_delay_count : 0
