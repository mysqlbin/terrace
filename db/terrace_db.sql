/*
Navicat MySQL Data Transfer

Source Server         : 192.168.0.54-3306
Source Server Version : 50722
Source Host           : 192.168.0.54:3306
Source Database       : terrace_db

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-04-04 16:28:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$mG2RsT12QURs$YFILWipOv28im9N0lM8eR3TQiiFMZ0awZP2anjXGM8I=', '2018-05-17 08:01:07.576051', '1', 'binbin', '', '', '1224056230@qq.com', '1', '1', '2018-05-04 04:08:25.419426');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$36000$iZGA5vpEmmSC$T2NdKrmrjF3qnwahvti3m+oqdhvrEHDQoJWhHw3VkzQ=', null, '0', 'public', '', '', '', '0', '1', '2018-05-04 04:20:43.102367');
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$100000$s8WR2hHpQMeY$wB2iYMp+WqNwRrooiISOgImKFa/7/dIdhPAudBSNH5M=', '2018-05-04 08:18:53.540426', '1', 'admin', '', '', 'rrrrrr', '1', '1', '2018-05-04 07:49:02.085113');

-- ----------------------------
-- Table structure for myapp_db_account
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_account`;
CREATE TABLE `myapp_db_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(30) NOT NULL,
  `passwd` varchar(255) NOT NULL,
  `role` varchar(30) NOT NULL,
  `tags` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_tages` (`tags`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account
-- ----------------------------
INSERT INTO `myapp_db_account` VALUES ('1', 'admin', '123456abc', 'admin', 'tags');
INSERT INTO `myapp_db_account` VALUES ('2', 'admins', '123456abc', 'admin', 'tags');

-- ----------------------------
-- Table structure for myapp_db_account_account
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_account_account`;
CREATE TABLE `myapp_db_account_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_account_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_accountID_userID` (`db_account_id`,`user_id`),
  KEY `idx_userID` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account_account
-- ----------------------------
INSERT INTO `myapp_db_account_account` VALUES ('1', '1', '3');

-- ----------------------------
-- Table structure for myapp_db_account_dbname
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_account_dbname`;
CREATE TABLE `myapp_db_account_dbname` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_account_id` int(11) NOT NULL,
  `db_name_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_accountID_nameID` (`db_account_id`,`db_name_id`),
  KEY `idx_name` (`db_name_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account_dbname
-- ----------------------------
INSERT INTO `myapp_db_account_dbname` VALUES ('1', '1', '1');

-- ----------------------------
-- Table structure for myapp_db_instance
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_instance`;
CREATE TABLE `myapp_db_instance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(30) NOT NULL,
  `port` varchar(10) NOT NULL,
  `role` varchar(30) NOT NULL,
  `db_type` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_ip_port` (`ip`,`port`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_instance
-- ----------------------------
INSERT INTO `myapp_db_instance` VALUES ('1', '192.168.0.54', '3306', 'admin', 'mysql');

-- ----------------------------
-- Table structure for myapp_db_name
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name`;
CREATE TABLE `myapp_db_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dbtag` varchar(30) NOT NULL,
  `dbname` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_dbtag` (`dbtag`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name
-- ----------------------------
INSERT INTO `myapp_db_name` VALUES ('1', 'backup_done_list', 'terrace_db');

-- ----------------------------
-- Table structure for myapp_db_name_account
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name_account`;
CREATE TABLE `myapp_db_name_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_name_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_nameID_userID` (`db_name_id`,`user_id`),
  KEY `idx_userID` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name_account
-- ----------------------------
INSERT INTO `myapp_db_name_account` VALUES ('3', '1', '3');
INSERT INTO `myapp_db_name_account` VALUES ('4', '2', '1');

-- ----------------------------
-- Table structure for myapp_db_name_instance
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name_instance`;
CREATE TABLE `myapp_db_name_instance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_name_id` int(11) NOT NULL,
  `db_instance_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_nameID_instanceID` (`db_name_id`,`db_instance_id`),
  KEY `idx_instanceID` (`db_instance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name_instance
-- ----------------------------
INSERT INTO `myapp_db_name_instance` VALUES ('1', '1', '1');
INSERT INTO `myapp_db_name_instance` VALUES ('2', '2', '1');

-- ----------------------------
-- Table structure for myapp_user_profile
-- ----------------------------
DROP TABLE IF EXISTS `myapp_user_profile`;
CREATE TABLE `myapp_user_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `select_limit` int(11) NOT NULL,
  `export_limit` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `task_email` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_userID` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_user_profile
-- ----------------------------

-- ----------------------------
-- Table structure for tb_blacklist
-- ----------------------------
DROP TABLE IF EXISTS `tb_blacklist`;
CREATE TABLE `tb_blacklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dbtag` varchar(255) NOT NULL,
  `tbname` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_dbtag` (`dbtag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tb_blacklist
-- ----------------------------

-- ----------------------------
-- Table structure for tb_blacklist_user_permit
-- ----------------------------
DROP TABLE IF EXISTS `tb_blacklist_user_permit`;
CREATE TABLE `tb_blacklist_user_permit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tb_blacklist_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_blacklistID_userID` (`tb_blacklist_id`,`user_id`),
  KEY `idx_userID` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tb_blacklist_user_permit
-- ----------------------------
