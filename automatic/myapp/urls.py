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
from django.urls import path
from myapp import views as myapp_view, instance, slowlog, binlog, polling, test, sqlquery,tests
from myapp.common import auth

app_name = ''

urlpatterns = [

    path('', myapp_view.index),

    path('index/', myapp_view.index, name='index'),

    path('slowquery/', myapp_view.slowquery, name='slowquery'),
    path('slowlog/slowquery_review/', slowlog.slowquery_review),
    path('slowlog/slowquery_review_history/', slowlog.slowquery_review_history),

    path('sqlquery/', myapp_view.sqlquery, name='sqlquery'),
    path('sqlquery/sql_query/', sqlquery.sql_query),

    path('pollingreport/', myapp_view.pollingreport, name='polling_report'),
    path('polling/polling_list/', polling.polling_list),
    # path('polling/get_polling_report/', polling.get_polling_report),
    path('polling/download_polling_report/', polling.download_polling_report),

    path('binlog2sql/', myapp_view.binlog2sql, name='binlog2sql'),
    path('binlog/binlog2sql/', binlog.binlog2sql),

    path('instance/', myapp_view.instance, name='instance'),
    path('instance/get_lists/', instance.get_lists),
    path('instance/get_instances_resource/', instance.get_instances_resource),
    path('instance/get_instance_name_id/', instance.get_instance_name_id),
    path('instance/get_instance_users/<id>/<instance_name>/', instance.get_instance_users, name='users'),

    path('instance/get_instances_binlog/', instance.get_instances_binlog),

    path('logoutView/', auth.logoutView),

    path('test/get_query_data/', test.get_query_data),

    path('tests/test01/', tests.test_01),
    path('tests/test02/', tests.test_02),
    # path('tests/test03/', tests.test_03),
    # path('tests/test04/', tests.test_04),
    path('tests/test05/', tests.test_05),
    path('tests/test06/', tests.test_06),
    path('tests/polling_test/', tests.polling_test),

]
