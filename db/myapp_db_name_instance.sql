/*
Navicat MySQL Data Transfer

Source Server         : 192.168.23.200_operation_all_user
Source Server Version : 50720
Source Host           : 192.168.23.200:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-17 16:35:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for myapp_db_name_instance
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name_instance`;
CREATE TABLE `myapp_db_name_instance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_name_id` int(11) NOT NULL,
  `db_instance_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_db_name_instance_db_name_id_db_instance_id_14cbcb24_uniq` (`db_name_id`,`db_instance_id`),
  KEY `myapp_db_name_instan_db_instance_id_d7d872ca_fk_myapp_db_` (`db_instance_id`),
  CONSTRAINT `myapp_db_name_instan_db_instance_id_d7d872ca_fk_myapp_db_` FOREIGN KEY (`db_instance_id`) REFERENCES `myapp_db_instance` (`id`),
  CONSTRAINT `myapp_db_name_instance_db_name_id_f7e01431_fk_myapp_db_name_id` FOREIGN KEY (`db_name_id`) REFERENCES `myapp_db_name` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name_instance
-- ----------------------------
INSERT INTO `myapp_db_name_instance` VALUES ('1', '1', '1');
INSERT INTO `myapp_db_name_instance` VALUES ('2', '2', '1');
