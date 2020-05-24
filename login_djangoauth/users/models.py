from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#继承AbstractUser，对原有的User表进行扩展，记得在setting中修改为AUTH_USER_MODEL = 'users.LoginUser'
class LoginUser(AbstractUser):
    '''
    用户表
    '''
    phone_numbers = models.CharField(verbose_name='手机号', unique=True,max_length=11, default='')

    def __str__(self):
        return self.username