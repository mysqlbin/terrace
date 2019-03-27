/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-17 15:01:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for myapp_db_account_account
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_account_account`;
CREATE TABLE `myapp_db_account_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_account_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_db_account_account_db_account_id_user_id_c376e49c_uniq` (`db_account_id`,`user_id`),
  KEY `myapp_db_account_account_user_id_9a520b3e_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_db_account_acc_db_account_id_efedf036_fk_myapp_db_` FOREIGN KEY (`db_account_id`) REFERENCES `myapp_db_account` (`id`),
  CONSTRAINT `myapp_db_account_account_user_id_9a520b3e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account_account
-- ----------------------------
INSERT INTO `myapp_db_account_account` VALUES ('1', '1', '3');
