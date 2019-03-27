/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-17 15:01:47
*/

SET FOREIGN_KEY_CHECKS=0;

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
  KEY `myapp_db_account_tags_d9e1181a` (`tags`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account
-- ----------------------------
INSERT INTO `myapp_db_account` VALUES ('1', 'admin', '123456abc', 'admin', 'tags');
