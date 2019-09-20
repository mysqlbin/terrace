
# 实现 MYAPP 的中文显示

from django.apps import AppConfig
import  os

# 修改 App在Admin 后台显示的名称
# default_app_config的值来自 apps.py 的类名
default_app_config = 'myapp.IndexConfig'

# 获取当前 App 的命名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

# 重写类 IndexConfig
class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '网站首页'
