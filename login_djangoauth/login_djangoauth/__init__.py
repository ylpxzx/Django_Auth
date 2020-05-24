from __future__ import absolute_import, unicode_literals

# 告诉Django在启动时别忘了检测我的celery文件
from .celery import app as celery_app
__all__ = ['celery_app']