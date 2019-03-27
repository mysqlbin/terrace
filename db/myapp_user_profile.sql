/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-21 17:37:56
*/

SET FOREIGN_KEY_CHECKS=0;

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
  UNIQUE KEY `user_id` (`user_id`),
  KEY `myapp_user_profile_task_email_950ac8fc` (`task_email`),
  CONSTRAINT `myapp_user_profile_user_id_0b750bc3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
