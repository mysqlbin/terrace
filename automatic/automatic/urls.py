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

app_name = ''

urlpatterns = [

    path('index/', myapp_view.index, name='index'),

    path('binlog_parse/', myapp_view.binlog_parse, name='binlog_parse'),
    path('slow_query/', myapp_view.slow_query, name='slow_query'),
    path('slowquery_review_history/<SQLId>/<startTime>/<endTime>/', myapp_view.slowquery_review_history, name='slowsql_info'),

    path('instance/', myapp_view.instance, name='instance'),
    path('ins_users/<id>/<instance_name>/', myapp_view.ins_users, name='users'),

    path('polling_report/', myapp_view.polling_report, name='polling_report'),

    # path('get_polling_report/<id>/<instance_name>/', myapp_view.get_polling_report, name='get_polling_report'),
    path('get_polling_report/', myapp_view.get_polling_report, name='get_polling_report'),

    # path('polling/', myapp_view.polling, name='polling'),

    # path('login/', myapp_view.login, name='login'),

    path('mysql_query/', myapp_view.mysql_query, name='mysql_query'),
    path('mysql_querys/', myapp_view.mysql_querys, name='mysql_querys'),

    # path('metas/', myapp_view.metas, name='metas'),

    path('binlog2sql/', myapp_view.binlog2sql, name='binlog2sql'),

    path('get_all_instances/', myapp_view.get_all_instances, name='get_polling'),

    path('get_instances_resource/', myapp_view.get_instances_resource, name='get_polling'),
    path('get_instances_binlog/', myapp_view.get_instances_binlog, name='get_polling'),


    # path('binlog/binlog2sql/', myapp_view.binlog2sql, name='get_polling'),
    path('get_binlog_to_sql/', myapp_view.get_binlog_to_sql, name='get_polling'),

    path('admin/', admin.site.urls),

]
