1.数据表巡检项:
1.1 统计数据库实例存储引擎的类型的数量:
table_schema:db1              engine:InnoDB                         engine_counts:              2 
table_schema:terrace_db       engine:InnoDB                         engine_counts:             24 
1.2 超过 1 G的大表:
###没有超过1 G的表###
1.3 数据量排名前 20 的表:
table_schema:terrace_db       table_name:auth_group_permissions         all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    0
table_schema:terrace_db       table_name:auth_user_groups               all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    0
table_schema:terrace_db       table_name:auth_user_user_permissions     all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    0
table_schema:terrace_db       table_name:django_admin_log               all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:   31
table_schema:terrace_db       table_name:myapp_db_account_account       all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    5
table_schema:terrace_db       table_name:myapp_db_account_dbname        all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    5
table_schema:terrace_db       table_name:myapp_db_name_account          all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    5
table_schema:terrace_db       table_name:myapp_db_name_instance         all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    5
table_schema:terrace_db       table_name:mysql_slow_query_review_history all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    7
table_schema:terrace_db       table_name:tb_blacklist_user_permit       all_size:0.02M           data_size:0.03M           index_size:0.05M           table_rows:    0
table_schema:terrace_db       table_name:auth_group                     all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:    0
table_schema:terrace_db       table_name:auth_permission                all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:   61
table_schema:terrace_db       table_name:auth_user                      all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:    2
table_schema:terrace_db       table_name:django_content_type            all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:   13
table_schema:terrace_db       table_name:django_session                 all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:   16
table_schema:terrace_db       table_name:myapp_db_account               all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:    5
table_schema:terrace_db       table_name:myapp_db_instance              all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:    6
table_schema:terrace_db       table_name:myapp_db_name                  all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:    6
table_schema:terrace_db       table_name:myapp_user_profile             all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:    0
table_schema:terrace_db       table_name:mysql_slow_query_review        all_size:0.02M           data_size:0.02M           index_size:0.03M           table_rows:    6
1.4 单表超过行数 10000000 表:
###没有单表超过行数 10000000 表###
1.5 自增ID占比大于 0.5 的表 :
###没有自增ID占比大于 0.5 的表###
1.6 碎片大于多少 0.01 的表 :
###没有碎片大于多少 0.01 的表###
1.7 统计大字段表:
###没有大字段表###
1.8 统计字段类型varchar长度大于 500 的表:
table_schema:db1             table_name:accountinfo                    column_name:Ip                             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:                 512
table_schema:db1             table_name:t                              column_name:c                              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:                 520
2.索引巡检项:
2.1 获取索引数目大于 5 个的表:
###没有索引数目大于5的表###
2.2 获取没有主键索引的表:
table_schema:db1              table_name:t                              
3.参数巡检项:
3.1 InnoDB层参数:
3.1.1 InnoDB层缓冲池参数:
innodb_random_read_ahead : OFF
innodb_read_ahead_threshold : 56
innodb_buffer_pool_load_at_startup : ON
innodb_buffer_pool_dump_at_shutdown : ON
innodb_flush_neighbors : 0
innodb_buffer_pool_size : 8589934592
innodb_buffer_pool_instances : 4
innodb_lru_scan_depth : 4000
innodb_max_dirty_pages_pct : 50.000000
innodb_old_blocks_pct : 37
innodb_old_blocks_time : 1000
3.1.2 InnoDB层redo参数:
innodb_flush_log_at_trx_commit : 1
innodb_log_file_size : 1073741824
innodb_log_files_in_group : 3
innodb_log_buffer_size : 33554432
3.1.3 InnoDB层持久化统计信息参数:
innodb_stats_persistent : ON
innodb_stats_persistent_sample_pages : 20
innodb_stats_auto_recalc : ON
3.1.4 InnoDB层其它参数:
innodb_rollback_on_timeout : ON
innodb_io_capacity : 4000
innodb_io_capacity_max : 8000
innodb_autoinc_lock_mode : 1
innodb_flush_method : O_DIRECT
innodb_file_per_table : ON
innodb_open_files : 65535
innodb_data_home_dir : 
innodb_lock_wait_timeout : 60
innodb_thread_concurrency : 0
innodb_fast_shutdown : 1
innodb_rollback_on_timeout : ON
innodb_data_file_path : ibdata1:1G:autoextend
innodb_write_io_threads : 8
innodb_read_io_threads : 8
innodb_purge_threads : 4
innodb_page_cleaners : 4
innodb_doublewrite : ON
innodb_change_buffer_max_size : 25
innodb_change_buffering : all
innodb_adaptive_hash_index : ON
3.2 Server层参数:
3.2.1 Server层binlog参数:
sync_binlog : 1
binlog_format : ROW
binlog_row_image : FULL
max_binlog_size : 1073741824
max_binlog_cache_size : 2147483648
expire_logs_days : 7
binlog_cache_size : 4194304
binlog_group_commit_sync_delay : 0
binlog_group_commit_sync_no_delay_count : 0
3.2.2 Server层线程/会话相关的内存参数:
key_buffer_size : 33554432
query_cache_size : 0
read_buffer_size : 8388608
read_rnd_buffer_size : 4194304
sort_buffer_size : 4194304
join_buffer_size : 4194304
tmp_table_size : 10240
3.2.3 Server层其它参数:
max_allowed_packet : 33554432
net_buffer_length : 16384
table_open_cache : 1024
max_execution_time : 0
sql_mode : STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION
interactive_timeout : 3600
wait_timeout : 3600
open_files_limit : 65535
lower_case_table_names : 1
slow_query_log : ON
long_query_time : 1.000000
log_queries_not_using_indexes : ON
system_time_zone : CST
time_zone : SYSTEM
log_timestamps : SYSTEM
max_connections : 512
max_connect_errors : 1000000
max_user_connections : 0
4. 状态巡检项:
4.1 InnoDB层缓冲池状态值:
Innodb_buffer_pool_pages_dirty : 13
Innodb_buffer_pool_pages_total : 524256
Innodb_buffer_pool_pages_data : 566
Innodb_buffer_pool_pages_flushed : 1365
Innodb_buffer_pool_read_requests : 57244
Innodb_buffer_pool_read_ahead : 0
Innodb_buffer_pool_read_ahead_evicted : 0
Innodb_buffer_pool_reads : 513
Innodb_buffer_pool_pages_free : 523685
Innodb_buffer_pool_wait_free : 0
脏页在缓冲池数据页中的占比为: 0.0%
InnoDB buffer pool 命中率: 99.11999999999999%
4.2 并发线程连接数:
Threads_connected : 3
Threads_created : 24
Threads_running : 1
4.3 InnoDB行锁等待:
Innodb_row_lock_current_waits : 0
Innodb_row_lock_time : 0
Innodb_row_lock_time_avg : 0
Innodb_row_lock_time_max : 0
Innodb_row_lock_waits : 0
4.4 打开表的次数:
Open_files : 25
Open_tables : 834
Opened_tables : 2391
4.5 创建内存临时表和磁盘临时表的次数:
Created_tmp_tables : 1977
Created_tmp_disk_tables : 934
4.6 InnoDB关键特性double write的使用情况:
Innodb_dblwr_pages_written : 143
Innodb_dblwr_writes : 53
每次写操作合并page的个数: 3.0
4.7 因log buffer不足导致等待的次数:
Innodb_log_waits : 0
5. 其它巡检项:
5.1 使用到内存临时表或者磁盘临时表的前 20 个SQL:
db_name:terrace_db           tmp_tables:226 tmp_disk_tables:226 tmp_all:452 last_seen:2019-09-02 03:49:32 query_sql:SHOW FULL TABLES 
db_name:terrace_db           tmp_tables:54 tmp_disk_tables:54 tmp_all:108 last_seen:2019-09-02 03:42:37 query_sql:SELECT `mysql_slow_query_revie ... _slow_query_review_history` . 
db_name:terrace_db           tmp_tables:22 tmp_disk_tables:22 tmp_all:44 last_seen:2019-09-02 03:42:37 query_sql:SELECT COUNT ( * ) FROM ( SELE ... ory` . `hostname_max` = ? AND 
db_name:terrace_db           tmp_tables:21 tmp_disk_tables:21 tmp_all:42 last_seen:2019-09-02 02:30:57 query_sql:SHOW STATUS 
db_name:information_schema   tmp_tables:38 tmp_disk_tables:0 tmp_all:38 last_seen:2019-09-02 03:42:37 query_sql:SHOW SCHEMAS 
db_name:terrace_db           tmp_tables:10 tmp_disk_tables:10 tmp_all:20 last_seen:2019-08-30 08:31:14 query_sql:SHOW FIELDS FROM `terrace_db` . `myapp_db_instance` 
db_name:information_schema   tmp_tables:9 tmp_disk_tables:9 tmp_all:18 last_seen:2019-08-30 06:37:26 query_sql:SELECT COLUMN_NAME , `COLLATIO ... ? ORDER BY `ORDINAL_POSITION` 
db_name:terrace_db           tmp_tables:8 tmp_disk_tables:8 tmp_all:16 last_seen:2019-09-02 03:42:46 query_sql:SELECT COUNT ( * ) FROM ( SELE ... query_review_history` WHERE ( 
db_name:terrace_db           tmp_tables:10 tmp_disk_tables:5 tmp_all:15 last_seen:2019-09-02 02:30:57 query_sql:SELECT `QUERY_ID` , SUM ( `DUR ... ROFILING` GROUP BY `QUERY_ID` 
db_name:terrace_db           tmp_tables:10 tmp_disk_tables:5 tmp_all:15 last_seen:2019-09-02 02:30:57 query_sql:SELECT `STATE` AS `状态` , `ROUN ... OUP BY `STATE` ORDER BY `SEQ` 
db_name:terrace_db           tmp_tables:6 tmp_disk_tables:6 tmp_all:12 last_seen:2019-09-02 02:31:51 query_sql:SHOW FIELDS FROM `terrace_db` . `mysql_slow_query_review` 
db_name:terrace_db           tmp_tables:6 tmp_disk_tables:6 tmp_all:12 last_seen:2019-09-02 02:30:41 query_sql:SHOW FIELDS FROM `terrace_db`  ... ql_slow_query_review_history` 
db_name:terrace_db           tmp_tables:5 tmp_disk_tables:5 tmp_all:10 last_seen:2019-09-02 02:30:30 query_sql:SHOW FULL TABLES FROM `terrace_db` WHERE `Table_type` != ? 
5.2 获取执行时间大于 1 秒的长事务:
没有执行时间大于 1 秒的长事务:
5.3 行锁等待列表:
没有行锁等待
