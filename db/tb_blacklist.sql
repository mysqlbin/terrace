/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-21 16:48:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_blacklist
-- ----------------------------
DROP TABLE IF EXISTS `tb_blacklist`;
CREATE TABLE `tb_blacklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dbtag` varchar(255) NOT NULL,
  `tbname` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dbtag` (`dbtag`)
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
  UNIQUE KEY `tb_blacklist_user_permit_tb_blacklist_id_user_id_12ae6db2_uniq` (`tb_blacklist_id`,`user_id`),
  KEY `tb_blacklist_user_permit_user_id_42b5c769_fk_auth_user_id` (`user_id`),
  CONSTRAINT `tb_blacklist_user_pe_tb_blacklist_id_3f1be554_fk_tb_blackl` FOREIGN KEY (`tb_blacklist_id`) REFERENCES `tb_blacklist` (`id`),
  CONSTRAINT `tb_blacklist_user_permit_user_id_42b5c769_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tb_blacklist_user_permit
-- ----------------------------
