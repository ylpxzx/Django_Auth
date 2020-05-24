from __future__ import absolute_import
import os
from celery import Celery

# 只要是想在自己的脚本中访问Django的数据库等文件就必须配置Django的环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login_djangoauth.settings') # login_djangoauth改为你的项目名

# app名字
app = Celery('login_djangoauth')  # login_djangoauth改为你的项目名

# 配置celery
class Config:
    BROKER_URL = 'redis://:你的redis密码@127.0.0.1:6379/2'  # 记得加上密码，不然会一直报错：RecursionError: maximum recursion depth exceeded in comparison
    CELERY_RESULT_BACKEND = 'redis://:你的redis密码@127.0.0.1:6379/3' # 格式：redis :// [: password@] host [: port] [/ database][? [timeout=timeout[d|h|m|s|ms|us|ns]] [&database=database]]

    CELERY_TIMEZONE = 'Asia/Shanghai'

    CELERY_ACCEPT_CONTENT = ['json', 'pickle']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'


app.config_from_object(Config)
# 到各个APP里自动发现tasks.py文件
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))