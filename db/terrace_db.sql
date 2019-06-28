/*
Navicat MySQL Data Transfer

Source Server         : 192.168.0.54-5.7
Source Server Version : 50722
Source Host           : 192.168.0.54:3306
Source Database       : terrace_db

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-06-28 18:33:09
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
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4;

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
INSERT INTO `auth_permission` VALUES ('19', 'Can add user_profile', '7', 'add_user_profile');
INSERT INTO `auth_permission` VALUES ('20', 'Can change user_profile', '7', 'change_user_profile');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete user_profile', '7', 'delete_user_profile');
INSERT INTO `auth_permission` VALUES ('22', 'can see mysql_query view', '7', 'can_mysql_query');
INSERT INTO `auth_permission` VALUES ('23', 'can see log_query view', '7', 'can_log_query');
INSERT INTO `auth_permission` VALUES ('24', 'can see mysql exec view', '7', 'can_see_execview');
INSERT INTO `auth_permission` VALUES ('25', 'can see inception view', '7', 'can_see_inception');
INSERT INTO `auth_permission` VALUES ('26', 'can see meta_data view', '7', 'can_see_metadata');
INSERT INTO `auth_permission` VALUES ('27', 'can see mysql_admin view', '7', 'can_see_mysqladmin');
INSERT INTO `auth_permission` VALUES ('28', 'can export csv', '7', 'can_export');
INSERT INTO `auth_permission` VALUES ('29', 'can insert mysql', '7', 'can_insert_mysql');
INSERT INTO `auth_permission` VALUES ('30', 'can update mysql', '7', 'can_update_mysql');
INSERT INTO `auth_permission` VALUES ('31', 'can delete mysql', '7', 'can_delete_mysql');
INSERT INTO `auth_permission` VALUES ('32', 'can create mysql', '7', 'can_create_mysql');
INSERT INTO `auth_permission` VALUES ('33', 'can drop mysql', '7', 'can_drop_mysql');
INSERT INTO `auth_permission` VALUES ('34', 'can truncate mysql', '7', 'can_truncate_mysql');
INSERT INTO `auth_permission` VALUES ('35', 'can alter mysql', '7', 'can_alter_mysql');
INSERT INTO `auth_permission` VALUES ('36', 'can query mongo', '7', 'can_query_mongo');
INSERT INTO `auth_permission` VALUES ('37', 'can see task view', '7', 'can_see_taskview');
INSERT INTO `auth_permission` VALUES ('38', 'can admin task', '7', 'can_admin_task');
INSERT INTO `auth_permission` VALUES ('39', 'can delete task', '7', 'can_delete_task');
INSERT INTO `auth_permission` VALUES ('40', 'can update task', '7', 'can_update_task');
INSERT INTO `auth_permission` VALUES ('41', 'can query pri', '7', 'can_query_pri');
INSERT INTO `auth_permission` VALUES ('42', 'can set pri', '7', 'can_set_pri');
INSERT INTO `auth_permission` VALUES ('43', 'can oper saltapi', '7', 'can_oper_saltapi');
INSERT INTO `auth_permission` VALUES ('44', 'Can add oper_log', '8', 'add_oper_log');
INSERT INTO `auth_permission` VALUES ('45', 'Can change oper_log', '8', 'change_oper_log');
INSERT INTO `auth_permission` VALUES ('46', 'Can delete oper_log', '8', 'delete_oper_log');
INSERT INTO `auth_permission` VALUES ('47', 'Can add db_account', '9', 'add_db_account');
INSERT INTO `auth_permission` VALUES ('48', 'Can change db_account', '9', 'change_db_account');
INSERT INTO `auth_permission` VALUES ('49', 'Can delete db_account', '9', 'delete_db_account');
INSERT INTO `auth_permission` VALUES ('50', 'Can add db_instance', '10', 'add_db_instance');
INSERT INTO `auth_permission` VALUES ('51', 'Can change db_instance', '10', 'change_db_instance');
INSERT INTO `auth_permission` VALUES ('52', 'Can delete db_instance', '10', 'delete_db_instance');
INSERT INTO `auth_permission` VALUES ('53', 'Can add db_name', '11', 'add_db_name');
INSERT INTO `auth_permission` VALUES ('54', 'Can change db_name', '11', 'change_db_name');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete db_name', '11', 'delete_db_name');
INSERT INTO `auth_permission` VALUES ('56', 'Can add saltrecord', '12', 'add_saltrecord');
INSERT INTO `auth_permission` VALUES ('57', 'Can change saltrecord', '12', 'change_saltrecord');
INSERT INTO `auth_permission` VALUES ('58', 'Can delete saltrecord', '12', 'delete_saltrecord');
INSERT INTO `auth_permission` VALUES ('59', 'Can add tb_blacklist', '13', 'add_tb_blacklist');
INSERT INTO `auth_permission` VALUES ('60', 'Can change tb_blacklist', '13', 'change_tb_blacklist');
INSERT INTO `auth_permission` VALUES ('61', 'Can delete tb_blacklist', '13', 'delete_tb_blacklist');
INSERT INTO `auth_permission` VALUES ('62', 'Can add 慢日志统计', '14', 'add_slowquery');
INSERT INTO `auth_permission` VALUES ('63', 'Can change 慢日志统计', '14', 'change_slowquery');
INSERT INTO `auth_permission` VALUES ('64', 'Can delete 慢日志统计', '14', 'delete_slowquery');
INSERT INTO `auth_permission` VALUES ('65', 'Can add 慢日志明细', '15', 'add_slowqueryhistory');
INSERT INTO `auth_permission` VALUES ('66', 'Can change 慢日志明细', '15', 'change_slowqueryhistory');
INSERT INTO `auth_permission` VALUES ('67', 'Can delete 慢日志明细', '15', 'delete_slowqueryhistory');

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
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$100000$s8WR2hHpQMeY$wB2iYMp+WqNwRrooiISOgImKFa/7/dIdhPAudBSNH5M=', '2019-06-28 10:54:16.949681', '1', 'admin', '', '', 'rrrrrr', '1', '1', '2018-05-04 07:49:02.085113');

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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-04-11 18:13:18.414143', '1', '192.168.0.54 write mysql', '1', '[{\"added\": {}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('2', '2019-04-11 18:14:15.024164', '1', '192.168.0.54 admin mysql', '2', '[{\"changed\": {\"fields\": [\"role\"]}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('3', '2019-04-11 18:15:16.740546', '1', 'sqldb sql_db', '1', '[{\"added\": {}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('4', '2019-04-11 18:16:25.820743', '1', 'sql_db all', '1', '[{\"added\": {}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('5', '2019-04-15 07:09:31.073112', '2', '192.168.0.252 admin mysql', '1', '[{\"added\": {}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('6', '2019-04-15 07:10:20.515297', '2', '252_test kpi', '1', '[{\"added\": {}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('7', '2019-04-15 07:11:00.493672', '2', '252_test admin', '1', '[{\"added\": {}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('8', '2019-04-16 05:10:56.348795', '3', '127.0.0.1 admin mysql', '1', '[{\"added\": {}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('9', '2019-04-16 05:11:24.333890', '3', 'master_nn niuniu_db', '1', '[{\"added\": {}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('10', '2019-04-16 05:11:48.517838', '3', 'admin_nn admin', '1', '[{\"added\": {}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('11', '2019-04-16 09:20:53.485476', '3', 'admin_nn admin', '2', '[{\"changed\": {\"fields\": [\"user\"]}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('12', '2019-04-16 09:21:08.792035', '2', '252_test admin', '2', '[{\"changed\": {\"fields\": [\"user\"]}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('13', '2019-04-16 09:42:43.710786', '4', '192.168.0.211 admin mysql', '1', '[{\"added\": {}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('14', '2019-04-16 09:43:06.008149', '4', '1rm niuniu_db', '1', '[{\"added\": {}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('15', '2019-04-16 09:43:56.118398', '4', '1rm_account admin', '1', '[{\"added\": {}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('16', '2019-04-16 09:44:37.983419', '4', '1rm_account admin', '2', '[]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('17', '2019-04-16 10:04:53.388160', '4', '1rm_account admin', '2', '[{\"changed\": {\"fields\": [\"user\", \"passwd\"]}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('18', '2019-04-16 10:16:20.259186', '5', 'localhost admin mysql', '1', '[{\"added\": {}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('19', '2019-04-16 10:16:51.956763', '5', 'yldb yldb', '1', '[{\"added\": {}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('20', '2019-04-16 10:17:52.496630', '5', 'yl_ admin', '1', '[{\"added\": {}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('21', '2019-04-16 10:18:41.487270', '5', 'localhost admin mysql', '3', '', '10', '3');
INSERT INTO `django_admin_log` VALUES ('22', '2019-04-16 10:18:49.740893', '5', 'yldb yldb', '3', '', '11', '3');
INSERT INTO `django_admin_log` VALUES ('23', '2019-04-16 10:18:58.203378', '5', 'yl_ admin', '3', '', '9', '3');
INSERT INTO `django_admin_log` VALUES ('24', '2019-04-16 18:41:34.081063', '6', '192.168.0.211 admin mysql', '1', '[{\"added\": {}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('25', '2019-04-16 18:42:52.352606', '6', '2rm niuniu_db', '1', '[{\"added\": {}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('26', '2019-04-16 18:43:40.524938', '6', '2rm_account admin', '1', '[{\"added\": {}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('27', '2019-04-18 09:49:33.367173', '7', '192.168.0.12 3306 admin1 mysql', '1', '[{\"added\": {}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('28', '2019-06-25 17:51:30.286681', '7', 'nnh5_recovery nnh5_recovery_db', '1', '[{\"added\": {}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('29', '2019-06-27 14:42:23.322181', '3', '生产环境 niuniu_db', '2', '[{\"changed\": {\"fields\": [\"dbtag\"]}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('30', '2019-06-27 16:57:34.745681', '1', '192.168.0.54 3306 admin1 mysql', '2', '[{\"changed\": {\"fields\": [\"type\", \"role\", \"charset\"]}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('31', '2019-06-27 16:58:51.064681', '3', '127.0.0.1 3306 admin mysql', '2', '[{\"changed\": {\"fields\": [\"instance_name\", \"type\", \"charset\"]}}]', '10', '3');
INSERT INTO `django_admin_log` VALUES ('32', '2019-06-27 17:13:26.733181', '1', '192.168.0.54 3306 admin mysql', '2', '[{\"changed\": {\"fields\": [\"type\", \"role\"]}}]', '10', '3');

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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('13', 'blacklist', 'tb_blacklist');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('9', 'myapp', 'db_account');
INSERT INTO `django_content_type` VALUES ('10', 'myapp', 'db_instance');
INSERT INTO `django_content_type` VALUES ('11', 'myapp', 'db_name');
INSERT INTO `django_content_type` VALUES ('8', 'myapp', 'oper_log');
INSERT INTO `django_content_type` VALUES ('14', 'myapp', 'slowquery');
INSERT INTO `django_content_type` VALUES ('15', 'myapp', 'slowqueryhistory');
INSERT INTO `django_content_type` VALUES ('7', 'myapp', 'user_profile');
INSERT INTO `django_content_type` VALUES ('12', 'salt', 'saltrecord');
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-04-11 17:04:32.824257');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-04-11 17:04:33.254102');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-04-11 17:04:33.366746');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-04-11 17:04:33.377324');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2019-04-11 17:04:33.470119');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2019-04-11 17:04:33.517437');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2019-04-11 17:04:33.534743');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2019-04-11 17:04:33.544188');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2019-04-11 17:04:33.601238');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2019-04-11 17:04:33.603474');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2019-04-11 17:04:33.614992');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2019-04-11 17:04:33.679739');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0009_alter_user_last_name_max_length', '2019-04-11 17:04:33.725635');
INSERT INTO `django_migrations` VALUES ('14', 'blacklist', '0001_initial', '2019-04-11 17:04:33.869333');
INSERT INTO `django_migrations` VALUES ('15', 'myapp', '0001_initial', '2019-04-11 17:04:34.584406');
INSERT INTO `django_migrations` VALUES ('16', 'salt', '0001_initial', '2019-04-11 17:04:34.617648');
INSERT INTO `django_migrations` VALUES ('17', 'sessions', '0001_initial', '2019-04-11 17:04:34.646980');
INSERT INTO `django_migrations` VALUES ('18', 'myapp', '0002_auto_20190627_1527', '2019-06-27 15:28:30.595181');
INSERT INTO `django_migrations` VALUES ('19', 'myapp', '0003_auto_20190627_1535', '2019-06-27 15:35:51.189181');
INSERT INTO `django_migrations` VALUES ('20', 'myapp', '0002_auto_20190627_1611', '2019-06-27 16:32:28.327181');
INSERT INTO `django_migrations` VALUES ('21', 'myapp', '0003_auto_20190627_1613', '2019-06-27 16:43:19.860181');

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
INSERT INTO `django_session` VALUES ('1omu0gj213xbbst2yo2yk30sqkw3bega', 'OGUzNTA1MWZiMGNjZjY3YzhkN2VmYjUzMWFjYTliMjdkZmQ5ZDc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwOTQ1OWUwYWRkMjI2Mzg1ZmNlNTVmOWZiZmUwYzEzOGE1YWM3Nzc0In0=', '2019-07-08 17:19:03.181000');
INSERT INTO `django_session` VALUES ('3dnxj1iul07crjblndhqh4nw02k39kii', 'N2E2MWE3YzBmOTYwODllYzg0Y2Q3Mjk1ZGYzNThiZDhmM2JjYWQ0ODp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDk0NTllMGFkZDIyNjM4NWZjZTU1ZjlmYmZlMGMxMzhhNWFjNzc3NCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2019-04-25 18:08:09.546155');
INSERT INTO `django_session` VALUES ('52k3soikxhejths6ghm2ao3v15rurpbt', 'OGUzNTA1MWZiMGNjZjY3YzhkN2VmYjUzMWFjYTliMjdkZmQ5ZDc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwOTQ1OWUwYWRkMjI2Mzg1ZmNlNTVmOWZiZmUwYzEzOGE1YWM3Nzc0In0=', '2019-07-11 14:31:38.538681');
INSERT INTO `django_session` VALUES ('688eln16jpxd9qkzjajsk6ppy7nj6urt', 'OGUzNTA1MWZiMGNjZjY3YzhkN2VmYjUzMWFjYTliMjdkZmQ5ZDc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwOTQ1OWUwYWRkMjI2Mzg1ZmNlNTVmOWZiZmUwYzEzOGE1YWM3Nzc0In0=', '2019-07-09 17:50:41.906681');
INSERT INTO `django_session` VALUES ('74k9uq6p1hcadv20czksvk3bjg1vnxhh', 'OGUzNTA1MWZiMGNjZjY3YzhkN2VmYjUzMWFjYTliMjdkZmQ5ZDc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwOTQ1OWUwYWRkMjI2Mzg1ZmNlNTVmOWZiZmUwYzEzOGE1YWM3Nzc0In0=', '2019-07-05 15:53:16.339000');
INSERT INTO `django_session` VALUES ('dfoo8v8kq77tc6b30gze4s0hiq1n95rx', 'ODIzZmZmMmRhMDBkMzhlYTFhYWIwMjQ1YmZjYTI2NzI4Y2UwMDRkYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2hhc2giOiIwOTQ1OWUwYWRkMjI2Mzg1ZmNlNTVmOWZiZmUwYzEzOGE1YWM3Nzc0In0=', '2019-04-29 06:59:57.834970');
INSERT INTO `django_session` VALUES ('h4iz00rjym38hwlaaaumuuw1vyxy1dwg', 'OGUzNTA1MWZiMGNjZjY3YzhkN2VmYjUzMWFjYTliMjdkZmQ5ZDc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwOTQ1OWUwYWRkMjI2Mzg1ZmNlNTVmOWZiZmUwYzEzOGE1YWM3Nzc0In0=', '2019-07-12 10:54:16.958181');
INSERT INTO `django_session` VALUES ('jeo9ehx58hq08gbsvd1cjr0uhuxevlds', 'OGUzNTA1MWZiMGNjZjY3YzhkN2VmYjUzMWFjYTliMjdkZmQ5ZDc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwOTQ1OWUwYWRkMjI2Mzg1ZmNlNTVmOWZiZmUwYzEzOGE1YWM3Nzc0In0=', '2019-07-04 09:44:41.880000');
INSERT INTO `django_session` VALUES ('ppw3odrnoxti971kxx48mmqrgn6frgut', 'N2E2MWE3YzBmOTYwODllYzg0Y2Q3Mjk1ZGYzNThiZDhmM2JjYWQ0ODp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDk0NTllMGFkZDIyNjM4NWZjZTU1ZjlmYmZlMGMxMzhhNWFjNzc3NCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2019-04-29 12:01:56.468721');
INSERT INTO `django_session` VALUES ('s3elkxb5cadlomvky5kph15m7j426a7k', 'OGUzNTA1MWZiMGNjZjY3YzhkN2VmYjUzMWFjYTliMjdkZmQ5ZDc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwOTQ1OWUwYWRkMjI2Mzg1ZmNlNTVmOWZiZmUwYzEzOGE1YWM3Nzc0In0=', '2019-07-10 12:05:14.443681');
INSERT INTO `django_session` VALUES ('ybb83p1bgy77u07kbi2bwuzmlt9ycxsz', 'N2E2MWE3YzBmOTYwODllYzg0Y2Q3Mjk1ZGYzNThiZDhmM2JjYWQ0ODp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDk0NTllMGFkZDIyNjM4NWZjZTU1ZjlmYmZlMGMxMzhhNWFjNzc3NCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2019-04-25 17:37:56.728486');

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account
-- ----------------------------
INSERT INTO `myapp_db_account` VALUES ('1', 'admin', '123456abc', 'all', 'sql_db');
INSERT INTO `myapp_db_account` VALUES ('2', 'paltform', 'ljb032@Ly2019%', 'admin', 'platform_252');
INSERT INTO `myapp_db_account` VALUES ('3', 'paltform', '123456abc', 'admin', 'platform_nn');
INSERT INTO `myapp_db_account` VALUES ('4', 'platform', 'G@8888%formplat', 'admin', '1rm_account');
INSERT INTO `myapp_db_account` VALUES ('6', 'platform', 'G@8888%formplat', 'admin', '2rm_account');

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account_account
-- ----------------------------
INSERT INTO `myapp_db_account_account` VALUES ('1', '1', '3');
INSERT INTO `myapp_db_account_account` VALUES ('2', '2', '3');
INSERT INTO `myapp_db_account_account` VALUES ('3', '3', '3');
INSERT INTO `myapp_db_account_account` VALUES ('4', '4', '3');
INSERT INTO `myapp_db_account_account` VALUES ('6', '6', '3');

-- ----------------------------
-- Table structure for myapp_db_account_dbname
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_account_dbname`;
CREATE TABLE `myapp_db_account_dbname` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_account_id` int(11) NOT NULL,
  `db_name_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_db_account_dbname_db_account_id_db_name_id_106a2af7_uniq` (`db_account_id`,`db_name_id`),
  KEY `myapp_db_account_dbname_db_name_id_693e2cb3_fk_myapp_db_name_id` (`db_name_id`),
  CONSTRAINT `myapp_db_account_dbn_db_account_id_b37f1a2b_fk_myapp_db_` FOREIGN KEY (`db_account_id`) REFERENCES `myapp_db_account` (`id`),
  CONSTRAINT `myapp_db_account_dbname_db_name_id_693e2cb3_fk_myapp_db_name_id` FOREIGN KEY (`db_name_id`) REFERENCES `myapp_db_name` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_account_dbname
-- ----------------------------
INSERT INTO `myapp_db_account_dbname` VALUES ('1', '1', '1');
INSERT INTO `myapp_db_account_dbname` VALUES ('2', '2', '2');
INSERT INTO `myapp_db_account_dbname` VALUES ('3', '3', '3');
INSERT INTO `myapp_db_account_dbname` VALUES ('4', '4', '4');
INSERT INTO `myapp_db_account_dbname` VALUES ('6', '6', '6');

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
  `instance_name` varchar(50) NOT NULL,
  `type` varchar(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_db_instance_ip_port_b37b05ac_uniq` (`ip`,`port`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_instance
-- ----------------------------
INSERT INTO `myapp_db_instance` VALUES ('1', '192.168.0.54', '3306', 'admin', 'mysql', 'utf8mb4', '2019-06-27 16:13:03.268681', '2019-06-27 16:13:07.190681', 'alone', '2019-06-27 17:13:26.727681');
INSERT INTO `myapp_db_instance` VALUES ('2', '192.168.0.252', '3306', 'admin', 'mysql', '', '2019-06-27 16:13:03.268681', '2019-06-27 16:13:07.190681', '', '2019-06-27 16:43:19.737681');
INSERT INTO `myapp_db_instance` VALUES ('3', '127.0.0.1', '3306', 'admin', 'mysql', 'utf8mb4', '2019-06-27 16:13:03.268681', 'nn主库', 'master', '2019-06-27 16:58:51.060681');
INSERT INTO `myapp_db_instance` VALUES ('4', '192.168.0.211', '2236', 'admin', 'mysql', '', '2019-06-27 16:13:03.268681', '2019-06-27 16:13:07.190681', '', '2019-06-27 16:43:19.737681');
INSERT INTO `myapp_db_instance` VALUES ('6', '192.168.0.211', '2307', 'admin', 'mysql', '', '2019-06-27 16:13:03.268681', '2019-06-27 16:13:07.190681', '', '2019-06-27 16:43:19.737681');
INSERT INTO `myapp_db_instance` VALUES ('7', '192.168.0.12', '3306', 'admin1', 'mysql', '', '2019-06-27 16:13:03.268681', '2019-06-27 16:13:07.190681', '', '2019-06-27 16:43:19.737681');

-- ----------------------------
-- Table structure for myapp_db_name
-- ----------------------------
DROP TABLE IF EXISTS `myapp_db_name`;
CREATE TABLE `myapp_db_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dbtag` varchar(30) NOT NULL,
  `dbname` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dbtag` (`dbtag`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name
-- ----------------------------
INSERT INTO `myapp_db_name` VALUES ('1', 'sqldb', 'sql_db');
INSERT INTO `myapp_db_name` VALUES ('2', '252_test', 'kpi');
INSERT INTO `myapp_db_name` VALUES ('3', '生产环境', 'niuniu_db');
INSERT INTO `myapp_db_name` VALUES ('4', '1rm', 'niuniu_db');
INSERT INTO `myapp_db_name` VALUES ('6', '2rm', 'niuniu_db');
INSERT INTO `myapp_db_name` VALUES ('7', 'nnh5_recovery', 'nnh5_recovery_db');

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name_account
-- ----------------------------
INSERT INTO `myapp_db_name_account` VALUES ('1', '1', '3');
INSERT INTO `myapp_db_name_account` VALUES ('2', '2', '3');
INSERT INTO `myapp_db_name_account` VALUES ('3', '3', '3');
INSERT INTO `myapp_db_name_account` VALUES ('4', '4', '3');
INSERT INTO `myapp_db_name_account` VALUES ('6', '6', '3');
INSERT INTO `myapp_db_name_account` VALUES ('7', '7', '3');

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_db_name_instance
-- ----------------------------
INSERT INTO `myapp_db_name_instance` VALUES ('1', '1', '1');
INSERT INTO `myapp_db_name_instance` VALUES ('2', '2', '2');
INSERT INTO `myapp_db_name_instance` VALUES ('3', '3', '3');
INSERT INTO `myapp_db_name_instance` VALUES ('4', '4', '4');
INSERT INTO `myapp_db_name_instance` VALUES ('6', '6', '6');
INSERT INTO `myapp_db_name_instance` VALUES ('7', '7', '3');

-- ----------------------------
-- Table structure for myapp_oper_log
-- ----------------------------
DROP TABLE IF EXISTS `myapp_oper_log`;
CREATE TABLE `myapp_oper_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(35) NOT NULL,
  `ipaddr` varchar(35) NOT NULL,
  `dbtag` varchar(35) NOT NULL,
  `dbname` varchar(40) NOT NULL,
  `sqltext` longtext NOT NULL,
  `sqltype` varchar(20) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `login_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_oper_log_dbtag_sqltype_create_time_cfafdbf7_idx` (`dbtag`,`sqltype`,`create_time`),
  KEY `myapp_oper_log_create_time_dd95545f` (`create_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_oper_log
-- ----------------------------

-- ----------------------------
-- Table structure for myapp_user_profile
-- ----------------------------
DROP TABLE IF EXISTS `myapp_user_profile`;
CREATE TABLE `myapp_user_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `select_limit` int(11) NOT NULL,
  `export_limit` int(11) NOT NULL,
  `task_email` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `myapp_user_profile_task_email_950ac8fc` (`task_email`),
  CONSTRAINT `myapp_user_profile_user_id_0b750bc3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myapp_user_profile
-- ----------------------------

-- ----------------------------
-- Table structure for mysql_slow_query_review
-- ----------------------------
DROP TABLE IF EXISTS `mysql_slow_query_review`;
CREATE TABLE `mysql_slow_query_review` (
  `checksum` char(32) NOT NULL,
  `fingerprint` longtext NOT NULL,
  `sample` longtext NOT NULL,
  `first_seen` datetime(6) DEFAULT NULL,
  `last_seen` datetime(6) DEFAULT NULL,
  `reviewed_by` varchar(20) DEFAULT NULL,
  `reviewed_on` datetime(6) DEFAULT NULL,
  `comments` longtext,
  `reviewed_status` varchar(24) DEFAULT NULL,
  PRIMARY KEY (`checksum`),
  KEY `idx_last_seen` (`last_seen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mysql_slow_query_review
-- ----------------------------
INSERT INTO `mysql_slow_query_review` VALUES ('1850FBAFDBFA571CED0464270F074159', 'insert into `archery`.`mysql_slow_query_review` (checksum, fingerprint, sample, first_seen, last_seen) values(?, ?, ?, coalesce(?, now()), coalesce(?, now())) on duplicate key update first_seen = if( first_seen is ?, coalesce(?, now()), least(first_seen, coalesce(?, now()))), last_seen = if( last_seen is ?, coalesce(?, now()), greatest(last_seen, coalesce(?, now())))', 'INSERT INTO `archery`.`mysql_slow_query_review`\n      (checksum, fingerprint, sample, first_seen, last_seen)\n      VALUES(\'ECAB6EE01072D556D1204D82C00FA836\', \'truncate table mysql_slow_query_review_history\', \'truncate table mysql_slow_query_review_history\', COALESCE(\'2019-06-20T15:34:56\', NOW()), COALESCE(\'2019-06-20T15:34:56\', NOW()))\n      ON DUPLICATE KEY UPDATE\n         first_seen = IF(\n            first_seen IS NULL,\n            COALESCE(\'2019-06-20T15:34:56\', NOW()),\n            LEAST(first_seen, COALESCE(\'2019-06-20T15:34:56\', NOW()))),\n         last_seen = IF(\n            last_seen IS NULL,\n            COALESCE(\'2019-06-20T15:34:56\', NOW()),\n            GREATEST(last_seen, COALESCE(\'2019-06-20T15:34:56\', NOW())))', '2019-06-20 15:35:14.000000', '2019-06-20 15:35:14.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('4DE8F9BE22101B637650CE16B73E38C7', 'truncate table mysql_slow_query_review', 'truncate table mysql_slow_query_review', '2019-06-20 15:34:56.000000', '2019-06-20 15:34:56.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('507A8C3C929392C00CD32C60BE1E87EA', 'show procedure status where db=?', 'SHOW PROCEDURE STATUS WHERE Db=\'archery\'', '2019-06-20 17:05:25.000000', '2019-06-20 17:14:21.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('751B6804D43917F6CFBAB7F3D65EB9CB', 'select * from table_clubgamescoredetail limit ?', 'select * from table_clubgamescoredetail limit 400000', '2019-06-20 15:35:09.000000', '2019-06-20 17:18:56.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('AC23D66D3AE55BD91029F67587660D2B', 'select `first_seen`, `last_seen`, `reviewed_by`, `reviewed_on`, `comments`, `reviewed_status`, checksum as checksum_conv from `archery`.`mysql_slow_query_review` where checksum=?', 'SELECT `first_seen`, `last_seen`, `reviewed_by`, `reviewed_on`, `comments`, `reviewed_status`, checksum AS checksum_conv FROM `archery`.`mysql_slow_query_review` WHERE checksum=\'ECAB6EE01072D556D1204D82C00FA836\'', '2019-06-20 15:35:14.000000', '2019-06-20 15:35:14.000000', null, null, null, null);
INSERT INTO `mysql_slow_query_review` VALUES ('ECAB6EE01072D556D1204D82C00FA836', 'truncate table mysql_slow_query_review_history', 'truncate table mysql_slow_query_review_history', '2019-06-20 15:34:56.000000', '2019-06-20 15:34:56.000000', null, null, null, null);

-- ----------------------------
-- Table structure for mysql_slow_query_review_history
-- ----------------------------
DROP TABLE IF EXISTS `mysql_slow_query_review_history`;
CREATE TABLE `mysql_slow_query_review_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname_max` varchar(64) NOT NULL,
  `client_max` varchar(64) DEFAULT NULL,
  `user_max` varchar(64) NOT NULL,
  `db_max` varchar(64) DEFAULT NULL,
  `checksum` char(32) NOT NULL,
  `sample` longtext NOT NULL,
  `ts_min` datetime(6) NOT NULL,
  `ts_max` datetime(6) NOT NULL,
  `ts_cnt` float DEFAULT NULL,
  `Query_time_sum` float DEFAULT NULL,
  `Query_time_min` float DEFAULT NULL,
  `Query_time_max` float DEFAULT NULL,
  `Query_time_pct_95` float DEFAULT NULL,
  `Query_time_stddev` float DEFAULT NULL,
  `Query_time_median` float DEFAULT NULL,
  `Lock_time_sum` float DEFAULT NULL,
  `Lock_time_min` float DEFAULT NULL,
  `Lock_time_max` float DEFAULT NULL,
  `Lock_time_pct_95` float DEFAULT NULL,
  `Lock_time_stddev` float DEFAULT NULL,
  `Lock_time_median` float DEFAULT NULL,
  `Rows_sent_sum` float DEFAULT NULL,
  `Rows_sent_min` float DEFAULT NULL,
  `Rows_sent_max` float DEFAULT NULL,
  `Rows_sent_pct_95` float DEFAULT NULL,
  `Rows_sent_stddev` float DEFAULT NULL,
  `Rows_sent_median` float DEFAULT NULL,
  `Rows_examined_sum` float DEFAULT NULL,
  `Rows_examined_min` float DEFAULT NULL,
  `Rows_examined_max` float DEFAULT NULL,
  `Rows_examined_pct_95` float DEFAULT NULL,
  `Rows_examined_stddev` float DEFAULT NULL,
  `Rows_examined_median` float DEFAULT NULL,
  `Rows_affected_sum` float DEFAULT NULL,
  `Rows_affected_min` float DEFAULT NULL,
  `Rows_affected_max` float DEFAULT NULL,
  `Rows_affected_pct_95` float DEFAULT NULL,
  `Rows_affected_stddev` float DEFAULT NULL,
  `Rows_affected_median` float DEFAULT NULL,
  `Rows_read_sum` float DEFAULT NULL,
  `Rows_read_min` float DEFAULT NULL,
  `Rows_read_max` float DEFAULT NULL,
  `Rows_read_pct_95` float DEFAULT NULL,
  `Rows_read_stddev` float DEFAULT NULL,
  `Rows_read_median` float DEFAULT NULL,
  `Merge_passes_sum` float DEFAULT NULL,
  `Merge_passes_min` float DEFAULT NULL,
  `Merge_passes_max` float DEFAULT NULL,
  `Merge_passes_pct_95` float DEFAULT NULL,
  `Merge_passes_stddev` float DEFAULT NULL,
  `Merge_passes_median` float DEFAULT NULL,
  `InnoDB_IO_r_ops_min` float DEFAULT NULL,
  `InnoDB_IO_r_ops_max` float DEFAULT NULL,
  `InnoDB_IO_r_ops_pct_95` float DEFAULT NULL,
  `InnoDB_IO_r_ops_stddev` float DEFAULT NULL,
  `InnoDB_IO_r_ops_median` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_min` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_max` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_pct_95` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_stddev` float DEFAULT NULL,
  `InnoDB_IO_r_bytes_median` float DEFAULT NULL,
  `InnoDB_IO_r_wait_min` float DEFAULT NULL,
  `InnoDB_IO_r_wait_max` float DEFAULT NULL,
  `InnoDB_IO_r_wait_pct_95` float DEFAULT NULL,
  `InnoDB_IO_r_wait_stddev` float DEFAULT NULL,
  `InnoDB_IO_r_wait_median` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_min` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_max` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_pct_95` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_stddev` float DEFAULT NULL,
  `InnoDB_rec_lock_wait_median` float DEFAULT NULL,
  `InnoDB_queue_wait_min` float DEFAULT NULL,
  `InnoDB_queue_wait_max` float DEFAULT NULL,
  `InnoDB_queue_wait_pct_95` float DEFAULT NULL,
  `InnoDB_queue_wait_stddev` float DEFAULT NULL,
  `InnoDB_queue_wait_median` float DEFAULT NULL,
  `InnoDB_pages_distinct_min` float DEFAULT NULL,
  `InnoDB_pages_distinct_max` float DEFAULT NULL,
  `InnoDB_pages_distinct_pct_95` float DEFAULT NULL,
  `InnoDB_pages_distinct_stddev` float DEFAULT NULL,
  `InnoDB_pages_distinct_median` float DEFAULT NULL,
  `QC_Hit_cnt` float DEFAULT NULL,
  `QC_Hit_sum` float DEFAULT NULL,
  `Full_scan_cnt` float DEFAULT NULL,
  `Full_scan_sum` float DEFAULT NULL,
  `Full_join_cnt` float DEFAULT NULL,
  `Full_join_sum` float DEFAULT NULL,
  `Tmp_table_cnt` float DEFAULT NULL,
  `Tmp_table_sum` float DEFAULT NULL,
  `Tmp_table_on_disk_cnt` float DEFAULT NULL,
  `Tmp_table_on_disk_sum` float DEFAULT NULL,
  `Filesort_cnt` float DEFAULT NULL,
  `Filesort_sum` float DEFAULT NULL,
  `Filesort_on_disk_cnt` float DEFAULT NULL,
  `Filesort_on_disk_sum` float DEFAULT NULL,
  `Bytes_sum` float DEFAULT NULL,
  `Bytes_min` float DEFAULT NULL,
  `Bytes_max` float DEFAULT NULL,
  `Bytes_pct_95` float DEFAULT NULL,
  `Bytes_stddev` float DEFAULT NULL,
  `Bytes_median` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `checksum` (`checksum`,`ts_min`,`ts_max`),
  KEY `idx_hostname_max_ts_min` (`hostname_max`,`ts_min`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mysql_slow_query_review_history
-- ----------------------------
INSERT INTO `mysql_slow_query_review_history` VALUES ('1', '127.0.0.1:3306', '127.0.0.1', 'root', 'niuniu_db', '751B6804D43917F6CFBAB7F3D65EB9CB', 'select * from table_clubgamescoredetail limit 400000', '2019-06-20 15:35:09.000000', '2019-06-20 15:35:09.000000', '1', '2.47095', '2.47095', '2.47095', '2.47095', '0', '2.47095', '0.000085', '0.000085', '0.000085', '0.000085', '0', '0.000085', '400000', '400000', '400000', '400000', '0', '400000', '400000', '400000', '400000', '400000', '0', '400000', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '52', '52', '52', '52', '0', '52');
INSERT INTO `mysql_slow_query_review_history` VALUES ('2', '39.108.17.15:3306', '121.35.101.4', 'root', 'niuniu_dbs', '4DE8F9BE22101B637650CE16B73E38C7', 'truncate table mysql_slow_query_review', '2019-06-20 15:34:56.000000', '2019-06-20 15:34:56.000000', '1', '0.033167', '0.033167', '0.033167', '0.033167', '0', '0.033167', '0.00029', '0.00029', '0.00029', '0.00029', '0', '0.00029', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '38', '38', '38', '38', '0', '38');
INSERT INTO `mysql_slow_query_review_history` VALUES ('3', '39.108.17.15:3306', '121.35.101.4', 'root', 'niuniu_dbs', 'ECAB6EE01072D556D1204D82C00FA836', 'truncate table mysql_slow_query_review_history', '2019-06-20 15:34:56.000000', '2019-06-20 15:34:56.000000', '1', '0.01473', '0.01473', '0.01473', '0.01473', '0', '0.01473', '0.000328', '0.000328', '0.000328', '0.000328', '0', '0.000328', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '46', '46', '46', '46', '0', '46');
INSERT INTO `mysql_slow_query_review_history` VALUES ('4', '39.108.17.15:3306', '127.0.0.1', 'root', 'niuniu_dbs', '751B6804D43917F6CFBAB7F3D65EB9CB', 'select * from table_clubgamescoredetail limit 400000', '2019-06-20 17:18:56.000000', '2019-06-20 17:18:56.000000', '1', '2.41457', '2.41457', '2.41457', '2.41457', '0', '2.41457', '0.000137', '0.000137', '0.000137', '0.000137', '0', '0.000137', '400000', '400000', '400000', '400000', '0', '400000', '400000', '400000', '400000', '400000', '0', '400000', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '52', '52', '52', '52', '0', '52');
INSERT INTO `mysql_slow_query_review_history` VALUES ('5', '39.108.17.15:3306', '121.35.101.4', 'root', 'niuniu_dbs', '507A8C3C929392C00CD32C60BE1E87EA', 'SHOW PROCEDURE STATUS WHERE Db=\'archery\'', '2019-06-20 17:05:25.000000', '2019-06-20 17:14:21.000000', '3', '0.094599', '0.031194', '0.032019', '0.031055', '0', '0.031055', '0.001095', '0.000322', '0.000423', '0.000403909', '0.0000360894', '0.000348912', '0', '0', '0', '0', '0', '0', '4620', '1540', '1540', '1540', '0', '1540', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '120', '40', '40', '40', '0', '40');
INSERT INTO `mysql_slow_query_review_history` VALUES ('6', '39.108.17.15:3306', '127.0.0.1', 'root', 'niuniu_dbs', '1850FBAFDBFA571CED0464270F074159', 'INSERT INTO `archery`.`mysql_slow_query_review`\n      (checksum, fingerprint, sample, first_seen, last_seen)\n      VALUES(\'ECAB6EE01072D556D1204D82C00FA836\', \'truncate table mysql_slow_query_review_history\', \'truncate table mysql_slow_query_review_history\', COALESCE(\'2019-06-20T15:34:56\', NOW()), COALESCE(\'2019-06-20T15:34:56\', NOW()))\n      ON DUPLICATE KEY UPDATE\n         first_seen = IF(\n            first_seen IS NULL,\n            COALESCE(\'2019-06-20T15:34:56\', NOW()),\n            LEAST(first_seen, COALESCE(\'2019-06-20T15:34:56\', NOW()))),\n         last_seen = IF(\n            last_seen IS NULL,\n            COALESCE(\'2019-06-20T15:34:56\', NOW()),\n            GREATEST(last_seen, COALESCE(\'2019-06-20T15:34:56\', NOW())))', '2019-06-20 15:35:14.000000', '2019-06-20 15:35:14.000000', '1', '0.014372', '0.014372', '0.014372', '0.014372', '0', '0.014372', '0.000103', '0.000103', '0.000103', '0.000103', '0', '0.000103', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '730', '730', '730', '730', '0', '730');
INSERT INTO `mysql_slow_query_review_history` VALUES ('7', '127.0.0.1:3306', '127.0.0.1', 'root', 'niuniu_dbs', 'AC23D66D3AE55BD91029F67587660D2B', 'SELECT `first_seen`, `last_seen`, `reviewed_by`, `reviewed_on`, `comments`, `reviewed_status`, checksum AS checksum_conv FROM `archery`.`mysql_slow_query_review` WHERE checksum=\'ECAB6EE01072D556D1204D82C00FA836\'', '2019-06-20 15:35:14.000000', '2019-06-20 15:35:14.000000', '1', '0.012613', '0.012613', '0.012613', '0.012613', '0', '0.012613', '0.000065', '0.000065', '0.000065', '0.000065', '0', '0.000065', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '211', '211', '211', '211', '0', '211');

-- ----------------------------
-- Table structure for salt_record
-- ----------------------------
DROP TABLE IF EXISTS `salt_record`;
CREATE TABLE `salt_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(30) NOT NULL,
  `operation` varchar(50) NOT NULL,
  `arg` longtext NOT NULL,
  `jid` varchar(255) NOT NULL,
  `tgt` varchar(100) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `salt_record_jid_5f70739c` (`jid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of salt_record
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
