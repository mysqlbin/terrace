from django.db import models
from django.contrib.auth.models import User
# Create your models here.

read_write = (
    ('read', 'read'),
    ('write', 'write'),
    ('all','all'),
    ('idle','idle'),
    #('admin','admin'),
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
        return u'%s %s %s' % (self.ip, self.role, self.db_type)
    class Meta:
        unique_together = ("ip", "port")


class Db_name (models.Model):
    dbtag = models.CharField(max_length=30, unique=True)
    dbname = models.CharField(max_length=30)
    instance = models.ManyToManyField(Db_instance)
    account = models.ManyToManyField(User)
    def __str__(self):
        return u'%s %s' % (self.dbtag, self.dbname)


class Db_account(models.Model):
    user = models.CharField(max_length=30)
    passwd = models.CharField(max_length=255)
    role =  models.CharField(max_length=30, choices=read_write_account,default='all')
    tags = models.CharField(max_length=30, db_index=True)
    dbname = models.ManyToManyField(Db_name)
    account = models.ManyToManyField(User)
    def __str__(self):
        return  u'%s %s' % ( self.tags, self.role)

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
        index_together = [["dbtag","sqltype", "create_time"],]

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