/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-17 15:01:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for myapp_db_account_dbname
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_account_dbname`;
CREATE TABLE `myapp_db_account_dbname` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_account_id` int(11) NOT NULL,
  `db_name_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_db_account_dbname_db_account_id_db_name_id_106a2af7_uniq` (`db_account_id`,`db_name_id`),
  KEY `myapp_db_account_dbname_db_name_id_693e2cb3_fk_myapp_db_name_id` (`db_name_id`),
  CONSTRAINT `myapp_db_account_dbn_db_account_id_b37f1a2b_fk_myapp_db_` FOREIGN KEY (`db_account_id`) REFERENCES `myapp_db_account` (`id`),
  CONSTRAINT `myapp_db_account_dbname_db_name_id_693e2cb3_fk_myapp_db_name_id` FOREIGN KEY (`db_name_id`) REFERENCES `myapp_db_name` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account_dbname
-- ----------------------------
INSERT INTO `myapp_db_account_dbname` VALUES ('1', '1', '1');
