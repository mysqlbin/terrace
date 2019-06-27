/*
Navicat MySQL Data Transfer

Source Server         : 192.168.0.54-5.7
Source Server Version : 50722
Source Host           : 192.168.0.54:3306
Source Database       : terrace_db

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-06-27 15:43:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for mysql_slow_query_review_history
-- ----------------------------
DROP TABLE IF EXISTS `mysql_slow_query_review_history`;
CREATE TABLE `mysql_slow_query_review_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname_max` varchar(64) NOT NULL,
  `client_max` varchar(64) DEFAULT NULL,
  `user_max` varchar(64) NOT NULL,
  `db_max` varchar(64) DEFAULT NULL,
  `checksum` char(32) NOT NULL,
  `sample` longtext NOT NULL,
  `ts_min` datetime(6) NOT NULL,
  `ts_max` datetime(6) NOT NULL,
  `ts_cnt` float DEFAULT NULL,
  `Query_time_sum` float DEFAULT NULL,
  `Query_time_min` float DEFAULT NULL,
  `Query_time_max` float DEFAULT NULL,
  `Query_time_pct_95` float DEFAULT NULL,
  `Query_time_stddev` float DEFAULT NULL,
  `Query_time_median` float DEFAULT NULL,
  `Lock_time_sum` float DEFAULT NULL,
  `Lock_time_min` float DEFAULT NULL,
  `Lock_time_max` float DEFAULT NULL,
  `Lock_time_pct_95` float DEFAULT NULL,
  `Lock_time_stddev` float DEFAULT NULL,
  `Lock_time_median` float DEFAULT NULL,
  `Rows_sent_sum` float DEFAULT NULL,
  `Rows_sent_min` float DEFAULT NULL,
  `Rows_sent_max` float DEFAULT NULL,
  `Rows_sent_pct_95` float DEFAULT NULL,
  `Rows_sent_stddev` float DEFAULT NULL,
  `Rows_sent_median` float DEFAULT NULL,
  `Rows_examined_sum` float DEFAULT NULL,
  `Rows_examined_min` float DEFAULT NULL,
  `Rows_examined_max` float DEFAULT NULL,
  `Rows_examined_pct_95` float DEFAULT NULL,
  `Rows_examined_stddev` float DEFAULT NULL,
  `Rows_examined_median` float DEFAULT NULL,
  `Rows_affected_sum` float DEFAULT NULL,
  `Rows_affected_min` float DEFAULT NULL,
  `Rows_affected_max` float DEFAULT NULL,
  `Rows_affected_pct_95` float DEFAULT NULL,
  `Rows_affected_stddev` float DEFAULT NULL,
  `Rows_affected_median` float DEFAULT NULL,
  `Rows_read_sum` float DEFAULT NULL,
  `Rows_read_min` float DEFAULT NULL,
  `Rows_read_max` float DEFAULT NULL,
  `Rows_read_pct_95` float DEFAULT NULL,
  `Rows_read_stddev` float DEFAULT NULL,
  `Rows_read_median` float DEFAULT NULL,
  `Merge_passes_sum` float DEFAULT NULL,
  `Merge_passes_min` float DEFAULT NULL,
  `Merge_passes_max` float DEFAULT NULL,
  `Merge_passes_pct_95` float DEFAULT NULL,
  `Merge_passes_stddev` float DEFAULT NULL,
  `Merge_passes_median` float DEFAULT NULL,
  `InnoDB_IO_r_ops_min` float DEFAULT NULL,
  `InnoDB_IO_r_ops_max` float DEFAULT NULL,
  `InnoDB_IO_r_ops_pct_95` float DEFAULT NULL,
  `InnoDB_IO_r_ops_stddev` float DEFAULT NULL,
  `InnoDB_IO_r_ops_median` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_min` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_max` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_pct_95` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_stddev` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_median` float DEFAULT NULL,
  `InnoDB_IO_r_wait_min` float DEFAULT NULL,
  `InnoDB_IO_r_wait_max` float DEFAULT NULL,
  `InnoDB_IO_r_wait_pct_95` float DEFAULT NULL,
  `InnoDB_IO_r_wait_stddev` float DEFAULT NULL,
  `InnoDB_IO_r_wait_median` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_min` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_max` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_pct_95` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_stddev` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_median` float DEFAULT NULL,
  `InnoDB_queue_wait_min` float DEFAULT NULL,
  `InnoDB_queue_wait_max` float DEFAULT NULL,
  `InnoDB_queue_wait_pct_95` float DEFAULT NULL,
  `InnoDB_queue_wait_stddev` float DEFAULT NULL,
  `InnoDB_queue_wait_median` float DEFAULT NULL,
  `InnoDB_pages_distinct_min` float DEFAULT NULL,
  `InnoDB_pages_distinct_max` float DEFAULT NULL,
  `InnoDB_pages_distinct_pct_95` float DEFAULT NULL,
  `InnoDB_pages_distinct_stddev` float DEFAULT NULL,
  `InnoDB_pages_distinct_median` float DEFAULT NULL,
  `QC_Hit_cnt` float DEFAULT NULL,
  `QC_Hit_sum` float DEFAULT NULL,
  `Full_scan_cnt` float DEFAULT NULL,
  `Full_scan_sum` float DEFAULT NULL,
  `Full_join_cnt` float DEFAULT NULL,
  `Full_join_sum` float DEFAULT NULL,
  `Tmp_table_cnt` float DEFAULT NULL,
  `Tmp_table_sum` float DEFAULT NULL,
  `Tmp_table_on_disk_cnt` float DEFAULT NULL,
  `Tmp_table_on_disk_sum` float DEFAULT NULL,
  `Filesort_cnt` float DEFAULT NULL,
  `Filesort_sum` float DEFAULT NULL,
  `Filesort_on_disk_cnt` float DEFAULT NULL,
  `Filesort_on_disk_sum` float DEFAULT NULL,
  `Bytes_sum` float DEFAULT NULL,
  `Bytes_min` float DEFAULT NULL,
  `Bytes_max` float DEFAULT NULL,
  `Bytes_pct_95` float DEFAULT NULL,
  `Bytes_stddev` float DEFAULT NULL,
  `Bytes_median` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `checksum` (`checksum`,`ts_min`,`ts_max`),
  KEY `idx_hostname_max_ts_min` (`hostname_max`,`ts_min`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mysql_slow_query_review_history
-- ----------------------------
INSERT INTO `mysql_slow_query_review_history` VALUES ('1', '39.108.17.17:3306', '39.108.17.17', 'root', 'niuniu_db', '751B6804D43917F6CFBAB7F3D65EB9CB', 'select * from table_clubgamescoredetail limit 400000', '2019-06-20 15:35:09.000000', '2019-06-20 15:35:09.000000', '1', '2.47095', '2.47095', '2.47095', '2.47095', '0', '2.47095', '0.000085', '0.000085', '0.000085', '0.000085', '0', '0.000085', '400000', '400000', '400000', '400000', '0', '400000', '400000', '400000', '400000', '400000', '0', '400000', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '52', '52', '52', '52', '0', '52');
INSERT INTO `mysql_slow_query_review_history` VALUES ('2', '39.108.17.15:3306', '121.35.101.4', 'root', 'niuniu_dbs', '4DE8F9BE22101B637650CE16B73E38C7', 'truncate table mysql_slow_query_review', '2019-06-20 15:34:56.000000', '2019-06-20 15:34:56.000000', '1', '0.033167', '0.033167', '0.033167', '0.033167', '0', '0.033167', '0.00029', '0.00029', '0.00029', '0.00029', '0', '0.00029', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '38', '38', '38', '38', '0', '38');
INSERT INTO `mysql_slow_query_review_history` VALUES ('3', '39.108.17.15:3306', '121.35.101.4', 'root', 'niuniu_dbs', 'ECAB6EE01072D556D1204D82C00FA836', 'truncate table mysql_slow_query_review_history', '2019-06-20 15:34:56.000000', '2019-06-20 15:34:56.000000', '1', '0.01473', '0.01473', '0.01473', '0.01473', '0', '0.01473', '0.000328', '0.000328', '0.000328', '0.000328', '0', '0.000328', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '46', '46', '46', '46', '0', '46');
INSERT INTO `mysql_slow_query_review_history` VALUES ('4', '39.108.17.15:3306', '39.108.17.17', 'root', 'niuniu_dbs', '751B6804D43917F6CFBAB7F3D65EB9CB', 'select * from table_clubgamescoredetail limit 400000', '2019-06-20 17:18:56.000000', '2019-06-20 17:18:56.000000', '1', '2.41457', '2.41457', '2.41457', '2.41457', '0', '2.41457', '0.000137', '0.000137', '0.000137', '0.000137', '0', '0.000137', '400000', '400000', '400000', '400000', '0', '400000', '400000', '400000', '400000', '400000', '0', '400000', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '52', '52', '52', '52', '0', '52');
INSERT INTO `mysql_slow_query_review_history` VALUES ('5', '39.108.17.15:3306', '121.35.101.4', 'root', 'niuniu_dbs', '507A8C3C929392C00CD32C60BE1E87EA', 'SHOW PROCEDURE STATUS WHERE Db=\'archery\'', '2019-06-20 17:05:25.000000', '2019-06-20 17:14:21.000000', '3', '0.094599', '0.031194', '0.032019', '0.031055', '0', '0.031055', '0.001095', '0.000322', '0.000423', '0.000403909', '0.0000360894', '0.000348912', '0', '0', '0', '0', '0', '0', '4620', '1540', '1540', '1540', '0', '1540', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '120', '40', '40', '40', '0', '40');
INSERT INTO `mysql_slow_query_review_history` VALUES ('6', '39.108.17.15:3306', '39.108.17.17', 'root', 'niuniu_dbs', '1850FBAFDBFA571CED0464270F074159', 'INSERT INTO `archery`.`mysql_slow_query_review`\n      (checksum, fingerprint, sample, first_seen, last_seen)\n      VALUES(\'ECAB6EE01072D556D1204D82C00FA836\', \'truncate table mysql_slow_query_review_history\', \'truncate table mysql_slow_query_review_history\', COALESCE(\'2019-06-20T15:34:56\', NOW()), COALESCE(\'2019-06-20T15:34:56\', NOW()))\n      ON DUPLICATE KEY UPDATE\n         first_seen = IF(\n            first_seen IS NULL,\n            COALESCE(\'2019-06-20T15:34:56\', NOW()),\n            LEAST(first_seen, COALESCE(\'2019-06-20T15:34:56\', NOW()))),\n         last_seen = IF(\n            last_seen IS NULL,\n            COALESCE(\'2019-06-20T15:34:56\', NOW()),\n            GREATEST(last_seen, COALESCE(\'2019-06-20T15:34:56\', NOW())))', '2019-06-20 15:35:14.000000', '2019-06-20 15:35:14.000000', '1', '0.014372', '0.014372', '0.014372', '0.014372', '0', '0.014372', '0.000103', '0.000103', '0.000103', '0.000103', '0', '0.000103', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '730', '730', '730', '730', '0', '730');
INSERT INTO `mysql_slow_query_review_history` VALUES ('7', '39.108.17.17:3306', '39.108.17.17', 'root', 'niuniu_dbs', 'AC23D66D3AE55BD91029F67587660D2B', 'SELECT `first_seen`, `last_seen`, `reviewed_by`, `reviewed_on`, `comments`, `reviewed_status`, checksum AS checksum_conv FROM `archery`.`mysql_slow_query_review` WHERE checksum=\'ECAB6EE01072D556D1204D82C00FA836\'', '2019-06-20 15:35:14.000000', '2019-06-20 15:35:14.000000', '1', '0.012613', '0.012613', '0.012613', '0.012613', '0', '0.012613', '0.000065', '0.000065', '0.000065', '0.000065', '0', '0.000065', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '211', '211', '211', '211', '0', '211');
