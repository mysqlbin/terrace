"""automatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views as myapp_view
from salt import views as salt_views

urlpatterns = [

    path('index/', myapp_view.index, name='index'),

    path('mysql_query/', myapp_view.mysql_query, name='mysql_query'),
    path('mysql_querys/', myapp_view.mysql_querys, name='mysql_querys'),

    path('metas/', myapp_view.metas, name='metas'),
    path('binlog_parse/', myapp_view.mysql_binlog_parse, name='binlog_parse'),
    #path('binlog_parse_test/', myapp_view.mysql_binlog_parse_test, name='binlog_parse_test'),
    #path('nav/', myapp_view.nav, name='nav'),

    #salt
    path('execute/', salt_views.execute, name='execute'),
    path('salt_exec/', salt_views.salt_exec, name='salt_exec'),
    path('api/getjobinfo/', salt_views.getjobinfo, name='getjobinfo'),
    path('hardware_info/', salt_views.hardware_info, name='hardware_info'),
    path('key_con/', salt_views.key_con, name='key_con'),
    path('salt_record/', salt_views.salt_record, name='salt_record'),
    path('record_detail/', salt_views.record_detail, name='record_detail'),

    #test, 用于调试
    path('test/', salt_views.test, name='test'),

    path('admin/', admin.site.urls),
]
