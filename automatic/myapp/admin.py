from django.contrib import admin
from myapp.models import Db_name,Db_account,Db_instance,User_profile
from django.contrib.auth.models import User


# Register your models here.
#通过 admin.site.register 注册模型类, 这样 admin 就可以管理数据库中这种类型的对象
admin.site.register(Db_instance)
admin.site.register(Db_name)
admin.site.register(Db_account)
admin.site.register(User_profile)


