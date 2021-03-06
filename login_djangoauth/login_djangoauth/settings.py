"""
Django settings for login_djangoauth project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from conf.aliyun_api import parser_config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sr-eb1z_-&2uc36*@u-^^^sdauqt^xe=n@vlt!%h@nid^f_vlg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'login_djangoauth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'static','templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':['django.templatetags.static'],
        },
    },
]

WSGI_APPLICATION = 'login_djangoauth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# MySQL数据库配置
res = parser_config('MySQL')
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': res['db'],
        'USER': res['user'],
        'PASSWORD': res['password'],
        'HOST': res['host'],
        'PORT': res['port'],
    }
}



# 配置redis缓存，短时间存储手机验证码
redis_cache = res = parser_config('Redis')
CAHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": redis_cache['LOCATION'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD": "密码",
            "DECODE_RESPONSES":True
        }
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# 配置静态文件路径
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static'),
)

AUTH_USER_MODEL = 'users.LoginUser'  # 扩展系统的用户表后记得添加此行

LOGIN_URL = '/login/'  # 想进入需要登录才能访问的页面时，如果你是未登录，将跳转到LOGIN_URL指定的登录界面

# AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend'] # 如果authenticate认证一直返回None的情况，可以加入该行
##authenticate认证一直返回None，可能是设置is_activate=False的原因，试着改为True


