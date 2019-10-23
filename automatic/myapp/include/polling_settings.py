
innodb_buffer_pool_param = [
    'innodb_random_read_ahead',
    'innodb_read_ahead_threshold',
    'innodb_buffer_pool_load_at_startup',
    'innodb_buffer_pool_dump_at_shutdown',
    'innodb_flush_neighbors',
    'innodb_buffer_pool_size',
    'innodb_buffer_pool_instances',
    'innodb_lru_scan_depth',
    'innodb_max_dirty_pages_pct',
    'innodb_old_blocks_pct',
    'innodb_old_blocks_time',
]

innodb_redo_log_param = [
    'innodb_flush_log_at_trx_commit',
    'innodb_log_file_size',
    'innodb_log_files_in_group',
    'innodb_log_buffer_size',
]

innodb_persistent_param = [
    'innodb_stats_persistent',
    'innodb_stats_persistent_sample_pages',
    'innodb_stats_auto_recalc',
]

innodb_other_param = [
    'innodb_rollback_on_timeout',
    'innodb_io_capacity',
    'innodb_io_capacity_max',
    'innodb_autoinc_lock_mode',
     'innodb_flush_method',
    'innodb_file_per_table',
    'innodb_open_files',
    'innodb_data_home_dir',
    'innodb_lock_wait_timeout',
    'innodb_thread_concurrency',
    'innodb_fast_shutdown',
    'innodb_rollback_on_timeout',
    'innodb_data_file_path',
    'innodb_write_io_threads',
    'innodb_read_io_threads',
    'innodb_purge_threads',
    'innodb_page_cleaners',
    'innodb_doublewrite',
    'innodb_change_buffer_max_size',
    'innodb_change_buffering',
    'innodb_adaptive_hash_index',
    'innodb_force_recovery',
]

server_binlog_param = [
    'sync_binlog',
    'binlog_format',
    'binlog_row_image',
    'max_binlog_size',
    'max_binlog_cache_size',
    'expire_logs_days',
    'binlog_cache_size',
    'binlog_group_commit_sync_delay',
    'binlog_group_commit_sync_no_delay_count',
    'binlog_transaction_dependency_tracking',
]

server_thread_session_param = [
    'key_buffer_size',
    'query_cache_size',
    'read_buffer_size',
    'read_rnd_buffer_size',
    'sort_buffer_size',
    'join_buffer_size',
    'tmp_table_size',
]

server_other_param = [
    'max_allowed_packet',
    'net_buffer_length',
    'table_open_cache',
    'max_execution_time',
    'sql_mode',
    'interactive_timeout',
    'wait_timeout',
    'open_files_limit',
    'lower_case_table_names',
    'slow_query_log',
    'long_query_time',
    'log_queries_not_using_indexes',
    'system_time_zone',
    'time_zone',
    'log_timestamps',
    'max_connections',
    'max_connect_errors',
    'max_user_connections',
]

innodb_buffer_pool_status_list = [
    'Innodb_buffer_pool_pages_dirty',
    'Innodb_buffer_pool_pages_total',
    'Innodb_buffer_pool_pages_data',
    'Innodb_buffer_pool_pages_flushed',
    'Innodb_buffer_pool_read_requests',
    'Innodb_buffer_pool_read_ahead',
    'Innodb_buffer_pool_read_ahead_evicted',
    'Innodb_buffer_pool_reads',
    'Innodb_buffer_pool_pages_free',
    'Innodb_buffer_pool_wait_free',
]

innodb_threads_connection_status_list = [
    'Threads_connected',
    'Threads_created',
    'Threads_running'
]

innodb_row_lock_status_list = [
    'Innodb_row_lock_current_waits',
    'Innodb_row_lock_time',
    'Innodb_row_lock_time_avg',
    'Innodb_row_lock_time_max',
    'Innodb_row_lock_waits',
]

innodb_open_status_list = [
    'Open_files',
    'Open_tables',
    'Opened_tables',
]

innodb_create_tmp_table_status_list = [
    'Created_tmp_tables',
    'Created_tmp_disk_tables'
]

innodb_double_write_status_list = [
    'Innodb_dblwr_pages_written',
    'Innodb_dblwr_writes',
]