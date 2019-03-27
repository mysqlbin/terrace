/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-17 16:21:06
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
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$36000$Sq6mnkPgIjWP$iDPCjKbEtsHTtDDKSwYyWmhnGQErF7LU9Hc6SdhBRLw=', '2018-05-04 08:18:53.540426', '1', 'admin_baks', '', '', 'rrrrrr', '1', '1', '2018-05-04 07:49:02.085113');
