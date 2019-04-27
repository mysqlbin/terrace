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

    path('binlog_parse/', myapp_view.binlog_parse, name='binlog_parse'),  # name:定义url名称

    path('login/', myapp_view.login, name='login'),

    path('mysql_query/', myapp_view.mysql_query, name='mysql_query'),
    path('mysql_querys/', myapp_view.mysql_querys, name='mysql_querys'),

    path('metas/', myapp_view.metas, name='metas'),


    path('admin/', admin.site.urls),

]
