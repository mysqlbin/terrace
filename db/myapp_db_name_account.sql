/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-17 16:35:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for myapp_db_name_account
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name_account`;
CREATE TABLE `myapp_db_name_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_name_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_db_name_account_db_name_id_user_id_71ab45fb_uniq` (`db_name_id`,`user_id`),
  KEY `myapp_db_name_account_user_id_894fb5ab_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_db_name_account_db_name_id_1c6af6de_fk_myapp_db_name_id` FOREIGN KEY (`db_name_id`) REFERENCES `myapp_db_name` (`id`),
  CONSTRAINT `myapp_db_name_account_user_id_894fb5ab_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name_account
-- ----------------------------
INSERT INTO `myapp_db_name_account` VALUES ('3', '1', '3');
INSERT INTO `myapp_db_name_account` VALUES ('4', '2', '1');
