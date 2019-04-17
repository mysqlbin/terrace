from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#创建模型来添加数据库服务
#每个模型被表示为 django.db.models.Model 类的子类
read_write = (
    ('read', 'read'),
    ('write', 'write'),
    ('all','all'),
    ('idle','idle'),
    ('admin','admin'),
)

read_write_account = (
    ('read', 'read'),
    ('write', 'write'),
    ('all','all'),
    ('admin','admin'),
)

class Db_instance(models.Model):
    ip = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    role = models.CharField(max_length=30, choices=read_write, )
    db_type = models.CharField(max_length=30, default='mysql')
    def __str__(self):
        return u'%s %s %s' % (self.ip, self.role, self.db_type)     #查询之后的返回值
    class Meta:          #创建唯一的联合索引
        unique_together = ("ip", "port")


class Db_name (models.Model):
    dbtag = models.CharField(max_length=30, unique=True)       #unique=True 表示创建唯一索引
    dbname = models.CharField(max_length=30)
    instance = models.ManyToManyField(Db_instance)   #查询时用于联表查询中的 on
    account = models.ManyToManyField(User)           #查询时用于联表查询中的 on
    def __str__(self):
        return u'%s %s' % (self.dbtag, self.dbname)

'''
SELECT
	`myapp_db_name`.`id`,
	`myapp_db_name`.`dbtag`,
	`myapp_db_name`.`dbname`
FROM
	`myapp_db_name`
INNER JOIN `myapp_db_name_instance` ON (
	`myapp_db_name`.`id` = `myapp_db_name_instance`.`db_name_id`
)
WHERE
	`myapp_db_name_instance`.`db_instance_id` = 1
'''


class Db_account(models.Model):
    user = models.CharField(max_length=30)
    passwd = models.CharField(max_length=255)
    role =  models.CharField(max_length=30, choices=read_write_account,default='all')
    tags = models.CharField(max_length=30, db_index=True)
    dbname = models.ManyToManyField(Db_name)
    account = models.ManyToManyField(User)
    def __str__(self):
        return  u'%s %s' % ( self.tags, self.role)

'''
SELECT
	`myapp_db_account`.`id`,
	`myapp_db_account`.`user`,
	`myapp_db_account`.`passwd`,
	`myapp_db_account`.`role`,
	`myapp_db_account`.`tags`
FROM
	`myapp_db_account`
INNER JOIN `myapp_db_account_dbname` ON (
	`myapp_db_account`.`id` = `myapp_db_account_dbname`.`db_account_id`
)
WHERE
	`myapp_db_account_dbname`.`db_name_id` = 1
'''
class Oper_log(models.Model):
    user = models.CharField(max_length=35)
    ipaddr = models.CharField(max_length=35)
    dbtag = models.CharField(max_length=35)
    dbname = models.CharField(max_length=40)
    sqltext = models.TextField()
    sqltype = models.CharField(max_length=20)
    create_time = models.DateTimeField(db_index=True)
    login_time = models.DateTimeField()
    def __str__(self):
        return self.dbtag
    class Meta:
        index_together = [["dbtag","sqltype", "create_time"],]        #三个字段的联合索引

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    select_limit = models.IntegerField(default=200)
    export_limit = models.IntegerField(default=200)
    task_email = models.IntegerField(db_index=True)
    def __str__(self):
        return  self.user.username
    class Meta:
        permissions =(('can_mysql_query','can see mysql_query view'),
                      ('can_log_query','can see log_query view'),
                      ('can_see_execview','can see mysql exec view'),
                      ('can_see_inception', 'can see inception view'),
                      ('can_see_metadata', 'can see meta_data view'),
                      ('can_see_mysqladmin', 'can see mysql_admin view'),
                      ('can_export','can export csv'),
                      ('can_insert_mysql','can insert mysql'),
                      ('can_update_mysql','can update mysql'),
                      ('can_delete_mysql','can delete mysql'),
                      ('can_create_mysql','can create mysql'),
                      ('can_drop_mysql','can drop mysql'),
                      ('can_truncate_mysql','can truncate mysql'),
                      ('can_alter_mysql','can alter mysql'),
                      ('can_query_mongo', 'can query mongo'),
                      ('can_see_taskview', 'can see task view'),
                      ('can_admin_task','can admin task'),
                      ('can_delete_task', 'can delete task'),
                      ('can_update_task', 'can update task'),
                      ('can_query_pri', 'can query pri'),
                      ('can_set_pri', 'can set pri'),
                      ('can_oper_saltapi', 'can oper saltapi'),
                      )