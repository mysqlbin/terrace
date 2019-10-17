

#获取慢日志统计
SELECT
	history.ts_max AS CreateTime,
	history.db_max AS dbname,
	fingerprint AS 'SQL语句',
	sum(history.query_time_sum) / sum(history.ts_cnt) AS '平均执行时长',
	sum(history.ts_cnt) AS '执行总次数',
	sum(history.query_time_sum) AS '执行总时长',
	sum(history.rows_examined_sum) AS '扫描总行数',
	sum(history.rows_sent_sum) AS '返回总行数'
FROM
	mysql_slow_query_review origin
JOIN mysql_slow_query_review_history history ON origin. `CHECKSUM` = history. `CHECKSUM` group by origin. `CHECKSUM`;


WHERE hostname_max = '' and 'db_max'




#获取慢日志明细
SELECT
	ts_min AS '执行开始时间',
	db_max AS '数据库名',
	user_max AS '用户名',
	sample AS 'SQL语句',
	ts_cnt AS '本次统计该sql语句出现的次数',
	query_time_pct_95 AS '本次统计该sql语句95%耗时',
	query_time_sum AS '本次统计该sql语句花费的总时间(秒)',
	lock_time_sum AS '本次统计该sql语句锁定总时长(秒)',
	rows_examined_sum AS '本次统计该sql语句解析总行数',
	rows_sent_sum AS '本次统计该sql语句返回总行数'
FROM
	mysql_slow_query_review_history;




