from django.contrib import admin
from myapp.models import Db_name,Db_account,Db_instance,User_profile
from django.contrib.auth.models import User


# Register your models here.

admin.site.register(Db_name)
admin.site.register(Db_account)
admin.site.register(Db_instance)
admin.site.register(User_profile)


