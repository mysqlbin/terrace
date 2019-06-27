from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#创建模型来添加数据库服务
#每个模型被表示为 django.db.models.Model 类的子类
read_write = (
    ('read1', 'read2'),
    ('write1', 'write2'),
    ('all1','all2'),
    ('idle1','idle2'),
    ('admin','admin'),
)

read_write_account = (
    ('read1', 'read2'),
    ('write1', 'write2'),
    ('all1','all2'),
    ('admin1','admin2'),
)

DB_TYPE_CHOICES = (
    ('mysql', 'MySQL'),
    ('mongodb', 'MongoDB'),
    ('mssql', 'MsSQL'),
    ('redis', 'Redis'),
    ('pgsql', 'PgSQL'),
    ('oracle', 'Oracle'))

INSTANCE_TYPE_CHOICES = (
    ('master', '主库'),
    ('slave', '从库'),
    ('alone', '单机'))

class Db_instance(models.Model):
    # instance_name = models.CharField('实例名称', max_length=50, unique=True)
    # type = models.CharField('实例类型', max_length=6, choices=(('master', '主库'), ('slave', '从库')))
    # db_type = models.CharField('数据库类型', max_length=30, default='mysql', choices=DB_TYPE_CHOICES, )
    # ip = models.CharField('IP地址', max_length=30)
    # port = models.CharField('端口号', max_length=10)
    # role = models.CharField('角色', max_length=30, choices=read_write, )
    # charset = models.CharField('字符集', max_length=20, default='', blank=True)
    # create_time = models.DateTimeField('创建时间', auto_now_add=True)
    # update_time = models.DateTimeField('更新时间', auto_now=True)

    instance_name = models.CharField(max_length=50, default='',)
    type = models.CharField( max_length=6, default='', choices=INSTANCE_TYPE_CHOICES,)
    db_type = models.CharField(max_length=30, default='mysql', choices=DB_TYPE_CHOICES, )
    ip = models.CharField( max_length=30)
    port = models.CharField(max_length=10)
    role = models.CharField(max_length=30, choices=read_write, )
    charset = models.CharField(max_length=20, default='', blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'%s %s %s %s' % (self.ip, self.port, self.role, self.db_type)     #查询之后的返回值
    class Meta:          #创建唯一的联合索引
        unique_together = ("ip", "port")


class Db_name (models.Model):
    dbtag = models.CharField(max_length=30, unique=True)       #unique=True 表示创建唯一索引
    dbname = models.CharField(max_length=30)
    instance = models.ManyToManyField(Db_instance)   #查询时用于联表查询中的 on
    account = models.ManyToManyField(User)           #查询时用于联表查询中的 on
    def __str__(self):
        return u'%s %s' % (self.dbtag, self.dbname)



class Db_account(models.Model):
    user = models.CharField(max_length=30)
    passwd = models.CharField(max_length=255)
    role =  models.CharField(max_length=30, choices=read_write_account,default='all2')
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



class SlowQuery(models.Model):
    """
    SlowQuery
    """
    checksum = models.CharField(max_length=32, primary_key=True)
    fingerprint = models.TextField()
    sample = models.TextField()
    first_seen = models.DateTimeField(blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True, db_index=True)
    reviewed_by = models.CharField(max_length=20, blank=True, null=True)
    reviewed_on = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_slow_query_review'
        verbose_name = u'慢日志统计'
        verbose_name_plural = u'慢日志统计'


class SlowQueryHistory(models.Model):
    """
    SlowQueryHistory
    """
    hostname_max = models.CharField(max_length=64, null=False)
    client_max = models.CharField(max_length=64, null=True)
    user_max = models.CharField(max_length=64, null=False)
    db_max = models.CharField(max_length=64, null=True, default=None)
    bytes_max = models.CharField(max_length=64, null=True)
    checksum = models.ForeignKey(SlowQuery, db_constraint=False, to_field='checksum', db_column='checksum',
                                 on_delete=models.CASCADE)
    sample = models.TextField()
    ts_min = models.DateTimeField(db_index=True)
    ts_max = models.DateTimeField()
    ts_cnt = models.FloatField(blank=True, null=True)
    query_time_sum = models.FloatField(db_column='Query_time_sum', blank=True, null=True)
    query_time_min = models.FloatField(db_column='Query_time_min', blank=True, null=True)
    query_time_max = models.FloatField(db_column='Query_time_max', blank=True, null=True)
    query_time_pct_95 = models.FloatField(db_column='Query_time_pct_95', blank=True, null=True)
    query_time_stddev = models.FloatField(db_column='Query_time_stddev', blank=True, null=True)
    query_time_median = models.FloatField(db_column='Query_time_median', blank=True, null=True)
    lock_time_sum = models.FloatField(db_column='Lock_time_sum', blank=True, null=True)
    lock_time_min = models.FloatField(db_column='Lock_time_min', blank=True, null=True)
    lock_time_max = models.FloatField(db_column='Lock_time_max', blank=True, null=True)
    lock_time_pct_95 = models.FloatField(db_column='Lock_time_pct_95', blank=True, null=True)
    lock_time_stddev = models.FloatField(db_column='Lock_time_stddev', blank=True, null=True)
    lock_time_median = models.FloatField(db_column='Lock_time_median', blank=True, null=True)
    rows_sent_sum = models.FloatField(db_column='Rows_sent_sum', blank=True, null=True)
    rows_sent_min = models.FloatField(db_column='Rows_sent_min', blank=True, null=True)
    rows_sent_max = models.FloatField(db_column='Rows_sent_max', blank=True, null=True)
    rows_sent_pct_95 = models.FloatField(db_column='Rows_sent_pct_95', blank=True, null=True)
    rows_sent_stddev = models.FloatField(db_column='Rows_sent_stddev', blank=True, null=True)
    rows_sent_median = models.FloatField(db_column='Rows_sent_median', blank=True, null=True)
    rows_examined_sum = models.FloatField(db_column='Rows_examined_sum', blank=True, null=True)
    rows_examined_min = models.FloatField(db_column='Rows_examined_min', blank=True, null=True)
    rows_examined_max = models.FloatField(db_column='Rows_examined_max', blank=True, null=True)
    rows_examined_pct_95 = models.FloatField(db_column='Rows_examined_pct_95', blank=True, null=True)
    rows_examined_stddev = models.FloatField(db_column='Rows_examined_stddev', blank=True, null=True)
    rows_examined_median = models.FloatField(db_column='Rows_examined_median', blank=True, null=True)
    rows_affected_sum = models.FloatField(db_column='Rows_affected_sum', blank=True, null=True)
    rows_affected_min = models.FloatField(db_column='Rows_affected_min', blank=True, null=True)
    rows_affected_max = models.FloatField(db_column='Rows_affected_max', blank=True, null=True)
    rows_affected_pct_95 = models.FloatField(db_column='Rows_affected_pct_95', blank=True, null=True)
    rows_affected_stddev = models.FloatField(db_column='Rows_affected_stddev', blank=True, null=True)
    rows_affected_median = models.FloatField(db_column='Rows_affected_median', blank=True, null=True)
    rows_read_sum = models.FloatField(db_column='Rows_read_sum', blank=True, null=True)
    rows_read_min = models.FloatField(db_column='Rows_read_min', blank=True, null=True)
    rows_read_max = models.FloatField(db_column='Rows_read_max', blank=True, null=True)
    rows_read_pct_95 = models.FloatField(db_column='Rows_read_pct_95', blank=True, null=True)
    rows_read_stddev = models.FloatField(db_column='Rows_read_stddev', blank=True, null=True)
    rows_read_median = models.FloatField(db_column='Rows_read_median', blank=True, null=True)
    merge_passes_sum = models.FloatField(db_column='Merge_passes_sum', blank=True, null=True)
    merge_passes_min = models.FloatField(db_column='Merge_passes_min', blank=True, null=True)
    merge_passes_max = models.FloatField(db_column='Merge_passes_max', blank=True, null=True)
    merge_passes_pct_95 = models.FloatField(db_column='Merge_passes_pct_95', blank=True, null=True)
    merge_passes_stddev = models.FloatField(db_column='Merge_passes_stddev', blank=True, null=True)
    merge_passes_median = models.FloatField(db_column='Merge_passes_median', blank=True, null=True)
    innodb_io_r_ops_min = models.FloatField(db_column='InnoDB_IO_r_ops_min', blank=True, null=True)
    innodb_io_r_ops_max = models.FloatField(db_column='InnoDB_IO_r_ops_max', blank=True, null=True)
    innodb_io_r_ops_pct_95 = models.FloatField(db_column='InnoDB_IO_r_ops_pct_95', blank=True, null=True)
    innodb_io_r_ops_stddev = models.FloatField(db_column='InnoDB_IO_r_ops_stddev', blank=True, null=True)
    innodb_io_r_ops_median = models.FloatField(db_column='InnoDB_IO_r_ops_median', blank=True, null=True)
    innodb_io_r_bytes_min = models.FloatField(db_column='InnoDB_IO_r_bytes_min', blank=True, null=True)
    innodb_io_r_bytes_max = models.FloatField(db_column='InnoDB_IO_r_bytes_max', blank=True, null=True)
    innodb_io_r_bytes_pct_95 = models.FloatField(db_column='InnoDB_IO_r_bytes_pct_95', blank=True, null=True)
    innodb_io_r_bytes_stddev = models.FloatField(db_column='InnoDB_IO_r_bytes_stddev', blank=True, null=True)
    innodb_io_r_bytes_median = models.FloatField(db_column='InnoDB_IO_r_bytes_median', blank=True, null=True)
    innodb_io_r_wait_min = models.FloatField(db_column='InnoDB_IO_r_wait_min', blank=True, null=True)
    innodb_io_r_wait_max = models.FloatField(db_column='InnoDB_IO_r_wait_max', blank=True, null=True)
    innodb_io_r_wait_pct_95 = models.FloatField(db_column='InnoDB_IO_r_wait_pct_95', blank=True, null=True)
    innodb_io_r_wait_stddev = models.FloatField(db_column='InnoDB_IO_r_wait_stddev', blank=True, null=True)
    innodb_io_r_wait_median = models.FloatField(db_column='InnoDB_IO_r_wait_median', blank=True, null=True)
    innodb_rec_lock_wait_min = models.FloatField(db_column='InnoDB_rec_lock_wait_min', blank=True, null=True)
    innodb_rec_lock_wait_max = models.FloatField(db_column='InnoDB_rec_lock_wait_max', blank=True, null=True)
    innodb_rec_lock_wait_pct_95 = models.FloatField(db_column='InnoDB_rec_lock_wait_pct_95', blank=True, null=True)
    innodb_rec_lock_wait_stddev = models.FloatField(db_column='InnoDB_rec_lock_wait_stddev', blank=True, null=True)
    innodb_rec_lock_wait_median = models.FloatField(db_column='InnoDB_rec_lock_wait_median', blank=True, null=True)
    innodb_queue_wait_min = models.FloatField(db_column='InnoDB_queue_wait_min', blank=True, null=True)
    innodb_queue_wait_max = models.FloatField(db_column='InnoDB_queue_wait_max', blank=True, null=True)
    innodb_queue_wait_pct_95 = models.FloatField(db_column='InnoDB_queue_wait_pct_95', blank=True, null=True)
    innodb_queue_wait_stddev = models.FloatField(db_column='InnoDB_queue_wait_stddev', blank=True, null=True)
    innodb_queue_wait_median = models.FloatField(db_column='InnoDB_queue_wait_median', blank=True, null=True)
    innodb_pages_distinct_min = models.FloatField(db_column='InnoDB_pages_distinct_min', blank=True, null=True)
    innodb_pages_distinct_max = models.FloatField(db_column='InnoDB_pages_distinct_max', blank=True, null=True)
    innodb_pages_distinct_pct_95 = models.FloatField(db_column='InnoDB_pages_distinct_pct_95', blank=True, null=True)
    innodb_pages_distinct_stddev = models.FloatField(db_column='InnoDB_pages_distinct_stddev', blank=True, null=True)
    innodb_pages_distinct_median = models.FloatField(db_column='InnoDB_pages_distinct_median', blank=True, null=True)
    qc_hit_cnt = models.FloatField(db_column='QC_Hit_cnt', blank=True, null=True)
    qc_hit_sum = models.FloatField(db_column='QC_Hit_sum', blank=True, null=True)
    full_scan_cnt = models.FloatField(db_column='Full_scan_cnt', blank=True, null=True)
    full_scan_sum = models.FloatField(db_column='Full_scan_sum', blank=True, null=True)
    full_join_cnt = models.FloatField(db_column='Full_join_cnt', blank=True, null=True)
    full_join_sum = models.FloatField(db_column='Full_join_sum', blank=True, null=True)
    tmp_table_cnt = models.FloatField(db_column='Tmp_table_cnt', blank=True, null=True)
    tmp_table_sum = models.FloatField(db_column='Tmp_table_sum', blank=True, null=True)
    tmp_table_on_disk_cnt = models.FloatField(db_column='Tmp_table_on_disk_cnt', blank=True, null=True)
    tmp_table_on_disk_sum = models.FloatField(db_column='Tmp_table_on_disk_sum', blank=True, null=True)
    filesort_cnt = models.FloatField(db_column='Filesort_cnt', blank=True, null=True)
    filesort_sum = models.FloatField(db_column='Filesort_sum', blank=True, null=True)
    filesort_on_disk_cnt = models.FloatField(db_column='Filesort_on_disk_cnt', blank=True, null=True)
    filesort_on_disk_sum = models.FloatField(db_column='Filesort_on_disk_sum', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_slow_query_review_history'
        unique_together = ('checksum', 'ts_min', 'ts_max')
        index_together = ('hostname_max', 'ts_min')
        verbose_name = u'慢日志明细'
        verbose_name_plural = u'慢日志明细'
