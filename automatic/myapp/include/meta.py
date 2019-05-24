#!/bin/env python
#-*-coding:utf-8-*-
import pymysql
import sys,string,time,datetime

def mysql_query(sql,user,passwd,host,port,dbname):

    conn=pymysql.connect(host=host,user=user,passwd=passwd,port=int(port),connect_timeout=5,charset='utf8')
    conn.select_db(dbname)
    cursor = conn.cursor()
    count=cursor.execute(sql)
    index=cursor.description
    col=[]
    #get column name

    for i in index:
        col.append(i[0])
    result=cursor.fetchall()
    # result=cursor.fetchmany(size=int(limitnum))
    cursor.close()
    conn.close()
    return (result,col)




def process(insname,flag=1,sql=''):
    if flag ==1:
        sql = 'select * from information_schema.processlist ORDER BY TIME DESC'
        return get_process_data(insname,sql)
    elif flag ==2:
        sql = "select * from information_schema.processlist where COMMAND!='Sleep' ORDER BY TIME DESC"
        return get_process_data(insname, sql)
    elif flag == 3:
        sql = "show engine innodb status"
        return get_process_data(insname, sql)
    elif flag == 5:
        sql = "show engine innodb mutex"
        return get_process_data(insname, sql)
    elif flag == 6:
        sql = "SELECT table_schema as 'DB',table_name as 'TABLE',CONCAT(ROUND(( data_length + index_length ) / ( 1024 * 1024 ), 2), '') 'TOTAL(M)' , table_comment as COMMENT FROM information_schema.TABLES ORDER BY data_length + index_length DESC limit 20;"
        return get_process_data(insname, sql)
    elif flag==7 :
        return get_process_data(insname, sql)
    elif flag == 8:
        sql = "select * from sys.schema_auto_increment_columns order by auto_increment_ratio desc limit 100"
        return get_process_data(insname, sql)


# def get_process_data(insname,sql):
#
#     results,col = mysql_query(sql,'salt_user','123456abc','127.0.0.1',3306,'information_schema')
#
#     return results,col


'''

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

CREATE TABLE `myapp_db_instance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(30) NOT NULL,
  `port` varchar(10) NOT NULL,
  `role` varchar(30) NOT NULL,
  `db_type` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_db_instance_ip_port_b37b05ac_uniq` (`ip`,`port`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `myapp_db_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dbtag` varchar(30) NOT NULL,
  `dbname` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dbtag` (`dbtag`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

insname.db_name_set.all:
SELECT `myapp_db_name`.`id`, `myapp_db_name`.`dbtag`, `myapp_db_name`.`dbname` FROM `myapp_db_name` INNER JOIN `myapp_db_name_instance` ON (`myapp_db_name`.`id` = `myapp_db_name_instance`.`db_name_id`) WHERE `myapp_db_name_instance`.`db_instance_id` = 1

a.db_account_set.all:
SELECT `myapp_db_account`.`id`, `myapp_db_account`.`user`, `myapp_db_account`.`passwd`, `myapp_db_account`.`role`, `myapp_db_account`.`tags` FROM `myapp_db_account` INNER JOIN `myapp_db_account_dbname` ON (`myapp_db_account`.`id` = `myapp_db_account_dbname`.`db_account_id`) WHERE `myapp_db_account_dbname`.`db_name_id` = 1



'''
def get_process_data(insname,sql):
    flag = True
    # pc = prpcrypt()
    #SELECT `myapp_db_name`.`id`, `myapp_db_name`.`dbtag`, `myapp_db_name`.`dbname` FROM `myapp_db_name` INNER JOIN `myapp_db_name_instance` ON (`myapp_db_name`.`id` = `myapp_db_name_instance`.`db_name_id`) WHERE `myapp_db_name_instance`.`db_instance_id` = 7; args=(7,)
    for a in insname.db_name_set.all():    #models.py：Db_name
        #SELECT `myapp_db_account`.`id`, `myapp_db_account`.`user`, `myapp_db_account`.`passwd`, `myapp_db_account`.`role`, `myapp_db_account`.`tags` FROM `myapp_db_account` INNER JOIN `myapp_db_account_dbname` ON (`myapp_db_account`.`id` = `myapp_db_account_dbname`.`db_account_id`) WHERE `myapp_db_account_dbname`.`db_name_id` = 2; args=(2,)
        for i in a.db_account_set.all():   #models.py：Db_account
            # if i.role == 'admin':         '''获取账号和密码，用来连接数据库'''
            tar_username = i.user
            tar_passwd = i.passwd
            flag = False
            break
        if flag == False:
            break
    if 'tar_username' in vars():
        try:
            results, col = mysql_query(sql,tar_username,tar_passwd,insname.ip,int(insname.port),'information_schema')
        except Exception as e:
            #防止失败，返回一个wrong_message
            results, col = ([str(e)], ''), ['error']
            #results,col = mysql_query(wrong_msg,user,passwd,host,int(port),dbname)
        return results, col
    else:
        return (['PLEASE set the admin role account FIRST'], ''), ['error']

'''
sql = "select * from mon_tbsize where DBTAG='" + dbtag + "' order by `TOTAL(M)` desc "
'''
