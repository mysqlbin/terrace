/*
Navicat MySQL Data Transfer

Source Server         : 192.168.0.54-5.7
Source Server Version : 50722
Source Host           : 192.168.0.54:3306
Source Database       : terrace_db

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-06-27 15:44:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for mysql_slow_query_review
-- ----------------------------
DROP TABLE IF EXISTS `mysql_slow_query_review`;
CREATE TABLE `mysql_slow_query_review` (
  `checksum` char(32) NOT NULL,
  `fingerprint` longtext NOT NULL,
  `sample` longtext NOT NULL,
  `first_seen` datetime(6) DEFAULT NULL,
  `last_seen` datetime(6) DEFAULT NULL,
  `reviewed_by` varchar(20) DEFAULT NULL,
  `reviewed_on` datetime(6) DEFAULT NULL,
  `comments` longtext,
  `reviewed_status` varchar(24) DEFAULT NULL,
  PRIMARY KEY (`checksum`),
  KEY `idx_last_seen` (`last_seen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mysql_slow_query_review
-- ----------------------------
INSERT INTO `mysql_slow_query_review` VALUES ('1850FBAFDBFA571CED0464270F074159', 'insert into `archery`.`mysql_slow_query_review` (checksum, fingerprint, sample, first_seen, last_seen) values(?, ?, ?, coalesce(?, now()), coalesce(?, now())) on duplicate key update first_seen = if( first_seen is ?, coalesce(?, now()), least(first_seen, coalesce(?, now()))), last_seen = if( last_seen is ?, coalesce(?, now()), greatest(last_seen, coalesce(?, now())))', 'INSERT INTO `archery`.`mysql_slow_query_review`\n      (checksum, fingerprint, sample, first_seen, last_seen)\n      VALUES(\'ECAB6EE01072D556D1204D82C00FA836\', \'truncate table mysql_slow_query_review_history\', \'truncate table mysql_slow_query_review_history\', COALESCE(\'2019-06-20T15:34:56\', NOW()), COALESCE(\'2019-06-20T15:34:56\', NOW()))\n      ON DUPLICATE KEY UPDATE\n         first_seen = IF(\n            first_seen IS NULL,\n            COALESCE(\'2019-06-20T15:34:56\', NOW()),\n            LEAST(first_seen, COALESCE(\'2019-06-20T15:34:56\', NOW()))),\n         last_seen = IF(\n            last_seen IS NULL,\n            COALESCE(\'2019-06-20T15:34:56\', NOW()),\n            GREATEST(last_seen, COALESCE(\'2019-06-20T15:34:56\', NOW())))', '2019-06-20 15:35:14.000000', '2019-06-20 15:35:14.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('4DE8F9BE22101B637650CE16B73E38C7', 'truncate table mysql_slow_query_review', 'truncate table mysql_slow_query_review', '2019-06-20 15:34:56.000000', '2019-06-20 15:34:56.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('507A8C3C929392C00CD32C60BE1E87EA', 'show procedure status where db=?', 'SHOW PROCEDURE STATUS WHERE Db=\'archery\'', '2019-06-20 17:05:25.000000', '2019-06-20 17:14:21.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('751B6804D43917F6CFBAB7F3D65EB9CB', 'select * from table_clubgamescoredetail limit ?', 'select * from table_clubgamescoredetail limit 400000', '2019-06-20 15:35:09.000000', '2019-06-20 17:18:56.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('AC23D66D3AE55BD91029F67587660D2B', 'select `first_seen`, `last_seen`, `reviewed_by`, `reviewed_on`, `comments`, `reviewed_status`, checksum as checksum_conv from `archery`.`mysql_slow_query_review` where checksum=?', 'SELECT `first_seen`, `last_seen`, `reviewed_by`, `reviewed_on`, `comments`, `reviewed_status`, checksum AS checksum_conv FROM `archery`.`mysql_slow_query_review` WHERE checksum=\'ECAB6EE01072D556D1204D82C00FA836\'', '2019-06-20 15:35:14.000000', '2019-06-20 15:35:14.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('ECAB6EE01072D556D1204D82C00FA836', 'truncate table mysql_slow_query_review_history', 'truncate table mysql_slow_query_review_history', '2019-06-20 15:34:56.000000', '2019-06-20 15:34:56.000000', null, null, null, null);
