

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 获取 settings.py 的配置信息
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjango.settings')


# 定义 Celery对象，并将项目配置信息加载到对象中
# Celery 的参数一般以 项目名命名
app = Celery('automatic')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()




