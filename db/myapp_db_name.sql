/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-17 15:00:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for myapp_db_name
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name`;
CREATE TABLE `myapp_db_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dbtag` varchar(30) NOT NULL,
  `dbname` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dbtag` (`dbtag`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name
-- ----------------------------
INSERT INTO `myapp_db_name` VALUES ('1', 'backup_done_list', 'test');
