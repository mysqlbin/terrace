/*
Navicat MySQL Data Transfer

Source Server         : 192.168.0.54-3306
Source Server Version : 50722
Source Host           : 192.168.0.54:3306
Source Database       : terrace_db

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-04-12 09:33:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add user', '3', 'add_user');
INSERT INTO `auth_permission` VALUES ('8', 'Can change user', '3', 'change_user');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete user', '3', 'delete_user');
INSERT INTO `auth_permission` VALUES ('10', 'Can add group', '4', 'add_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can change group', '4', 'change_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete group', '4', 'delete_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');

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
  `last_name` varchar(150) NOT NULL,
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
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$100000$s8WR2hHpQMeY$wB2iYMp+WqNwRrooiISOgImKFa/7/dIdhPAudBSNH5M=', '2019-04-11 00:57:26.370981', '1', 'admin', '', '', 'rrrrrr', '1', '1', '2018-05-04 07:49:02.085113');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-04-11 00:59:35.058072', '2', '192.168.0.252 all mysql', '1', '[{\"added\": {}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('2', '2019-04-11 01:01:34.392878', '2', 'tags niuniu_db', '1', '[{\"added\": {}}]', '8', '3');
INSERT INTO `django_admin_log` VALUES ('3', '2019-04-11 01:07:01.591535', '3', '252_user admin', '1', '[{\"added\": {}}]', '7', '3');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('7', 'myapp', 'db_account');
INSERT INTO `django_content_type` VALUES ('9', 'myapp', 'db_instance');
INSERT INTO `django_content_type` VALUES ('8', 'myapp', 'db_name');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-04-11 00:37:33.709133');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-04-11 00:38:03.410208');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-04-11 00:38:03.531721');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-04-11 00:38:03.541034');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2019-04-11 00:38:03.630216');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2019-04-11 00:38:03.675589');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2019-04-11 00:38:03.690093');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2019-04-11 00:38:03.701536');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2019-04-11 00:38:03.747465');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2019-04-11 00:38:03.750031');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2019-04-11 00:38:03.762746');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2019-04-11 00:38:03.817182');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0009_alter_user_last_name_max_length', '2019-04-11 00:38:03.862378');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2019-04-11 00:38:03.893850');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('xnmknowvyjg52wabg8u1vqc9tsgkmgv3', 'MDM0NmIxOGUwZmYwNjI0NzY4ZjcwYzYzYTAzNTZlMDJlYTAyNTM4Njp7Il9hdXRoX3VzZXJfaGFzaCI6IjA5NDU5ZTBhZGQyMjYzODVmY2U1NWY5ZmJmZTBjMTM4YTVhYzc3NzQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=', '2019-04-25 00:57:26.374015');

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
  KEY `idx_tages` (`tags`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account
-- ----------------------------
INSERT INTO `myapp_db_account` VALUES ('1', 'admin', '123456abc', 'admin', 'tags');
INSERT INTO `myapp_db_account` VALUES ('2', 'admins', '123456abc', 'admin', 'tags');
INSERT INTO `myapp_db_account` VALUES ('3', 'manager', 'manager@c5c46e', 'admin', '252_user');

-- ----------------------------
-- Table structure for myapp_db_account_account
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_account_account`;
CREATE TABLE `myapp_db_account_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_account_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_accountID_userID` (`db_account_id`,`user_id`),
  KEY `idx_userID` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account_account
-- ----------------------------
INSERT INTO `myapp_db_account_account` VALUES ('1', '1', '3');
INSERT INTO `myapp_db_account_account` VALUES ('2', '3', '3');

-- ----------------------------
-- Table structure for myapp_db_account_dbname
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_account_dbname`;
CREATE TABLE `myapp_db_account_dbname` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_account_id` int(11) NOT NULL,
  `db_name_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_accountID_nameID` (`db_account_id`,`db_name_id`),
  KEY `idx_name` (`db_name_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account_dbname
-- ----------------------------
INSERT INTO `myapp_db_account_dbname` VALUES ('1', '1', '1');
INSERT INTO `myapp_db_account_dbname` VALUES ('2', '3', '2');

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
  UNIQUE KEY `idx_ip_port` (`ip`,`port`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_instance
-- ----------------------------
INSERT INTO `myapp_db_instance` VALUES ('1', '192.168.0.54', '3306', 'admin', 'mysql');
INSERT INTO `myapp_db_instance` VALUES ('2', '192.168.0.252', '3306', 'admin', 'mysql');

-- ----------------------------
-- Table structure for myapp_db_name
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name`;
CREATE TABLE `myapp_db_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dbtag` varchar(30) NOT NULL,
  `dbname` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_dbtag` (`dbtag`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name
-- ----------------------------
INSERT INTO `myapp_db_name` VALUES ('1', 'backup_done_list', 'terrace_db');
INSERT INTO `myapp_db_name` VALUES ('2', 'tags', 'niuniu_db');

-- ----------------------------
-- Table structure for myapp_db_name_account
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name_account`;
CREATE TABLE `myapp_db_name_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_name_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_nameID_userID` (`db_name_id`,`user_id`),
  KEY `idx_userID` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name_account
-- ----------------------------
INSERT INTO `myapp_db_name_account` VALUES ('3', '1', '3');
INSERT INTO `myapp_db_name_account` VALUES ('5', '2', '3');

-- ----------------------------
-- Table structure for myapp_db_name_instance
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name_instance`;
CREATE TABLE `myapp_db_name_instance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_name_id` int(11) NOT NULL,
  `db_instance_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_nameID_instanceID` (`db_name_id`,`db_instance_id`),
  KEY `idx_instanceID` (`db_instance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name_instance
-- ----------------------------
INSERT INTO `myapp_db_name_instance` VALUES ('1', '1', '1');
INSERT INTO `myapp_db_name_instance` VALUES ('3', '2', '2');

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
  UNIQUE KEY `idx_userID` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_user_profile
-- ----------------------------

-- ----------------------------
-- Table structure for tb_blacklist
-- ----------------------------
DROP TABLE IF EXISTS `tb_blacklist`;
CREATE TABLE `tb_blacklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dbtag` varchar(255) NOT NULL,
  `tbname` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_dbtag` (`dbtag`)
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
  UNIQUE KEY `idx_blacklistID_userID` (`tb_blacklist_id`,`user_id`),
  KEY `idx_userID` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tb_blacklist_user_permit
-- ----------------------------
