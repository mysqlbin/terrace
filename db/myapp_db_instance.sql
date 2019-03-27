/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-17 14:26:12
*/

SET FOREIGN_KEY_CHECKS=0;

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
  UNIQUE KEY `myapp_db_instance_ip_port_b37b05ac_uniq` (`ip`,`port`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_instance
-- ----------------------------
INSERT INTO `myapp_db_instance` VALUES ('1', '192.168.23.200', '3306', 'admin', 'mysql');
