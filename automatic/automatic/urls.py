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
from myapp import views as myapp_view, instance, slowlog, binlog, polling

app_name = ''

urlpatterns = [

    path('index/', myapp_view.index, name='index'),


    path('slow_query/', myapp_view.slow_query, name='slow_query'),
    path('slowlog/slowquery_review/', slowlog.slowquery_review),
    path('slowlog/slowquery_review_history/', slowlog.slowquery_review_history),


    path('polling_report/', myapp_view.polling_report, name='polling_report'),
    path('polling/polling_list/', polling.polling_list),
    path('polling/get_polling_report/', polling.get_polling_report),


    # path('login/', myapp_view.login, name='login'),

    # path('metas/', myapp_view.metas, name='metas'),

    path('binlog2sql/', myapp_view.binlog2sql, name='binlog2sql'),
    path('binlog/binlog2sql/', binlog.binlog2sql),

    path('instance/', myapp_view.instance, name='instance'),
    path('instance/get_lists/', instance.get_lists),
    path('instance/get_instances_resource/', instance.get_instances_resource),
    path('instance/get_instance_name_id/', instance.get_instance_name_id),
    path('instance/get_instance_users/<id>/<instance_name>/', instance.get_instance_users, name='users'),


    path('instance/get_instances_binlog/', instance.get_instances_binlog, name='get_polling'),




    #test
    path('index/', myapp_view.index, name='index'),


    path('admin/', admin.site.urls),

]
