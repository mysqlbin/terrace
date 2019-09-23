from django.contrib import admin
from myapp.models import Db_name,Db_account,Db_instance
from django.contrib.auth.models import User


# Register your models here.
#通过 admin.site.register 注册模型类, 这样 admin 就可以管理数据库中这种类型的对象

# 实例列表
@admin.register(Db_instance)
class DbinstanceAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'instance_name', 'type', 'db_type', 'ip', 'port', 'charset', 'create_time']

    search_fields = ['instance_name']

    list_filter = ['instance_name']

# 数据库列表
@admin.register(Db_name)
class DbnameAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'dbname', 'dbtag']

# 用户列表
@admin.register(Db_account)
class DbaccountAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'user', 'tags']




