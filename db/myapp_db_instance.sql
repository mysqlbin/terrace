/*
Navicat MySQL Data Transfer

Source Server         : 192.168.0.54-5.7
Source Server Version : 50722
Source Host           : 192.168.0.54:3306
Source Database       : terrace_db

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-06-27 16:36:53
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
  `charset` varchar(20) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_db_instance_ip_port_b37b05ac_uniq` (`ip`,`port`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_instance
-- ----------------------------
INSERT INTO `myapp_db_instance` VALUES ('1', '192.168.0.54', '3306', 'admin', 'mysql', '', '2019-06-27 16:13:03.268681');
INSERT INTO `myapp_db_instance` VALUES ('2', '192.168.0.252', '3306', 'admin', 'mysql', '', '2019-06-27 16:13:03.268681');
INSERT INTO `myapp_db_instance` VALUES ('3', '39.108.17.17', '3306', 'admin', 'mysql', '', '2019-06-27 16:13:03.268681');
INSERT INTO `myapp_db_instance` VALUES ('4', '192.168.0.211', '2236', 'admin', 'mysql', '', '2019-06-27 16:13:03.268681');
INSERT INTO `myapp_db_instance` VALUES ('6', '192.168.0.211', '2307', 'admin', 'mysql', '', '2019-06-27 16:13:03.268681');
INSERT INTO `myapp_db_instance` VALUES ('7', '192.168.0.12', '3306', 'admin1', 'mysql', '', '2019-06-27 16:13:03.268681');
