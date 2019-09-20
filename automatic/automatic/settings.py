"""
Django settings for automatic project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

CELERY_IMPORTS = ("myapp.tasks","myapp.include.scheduled","myapp.include.mon")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 密钥配置, 是一个随机值,在项目创建的时候自动生成
SECRET_KEY = '^1=x14ssj+#$imr^sv*=a!%s_olv^r@7#dhm-+=4=m2kg$zoo('

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式
DEBUG = True

# 允许所有的域名访问
ALLOWED_HOSTS = ['*']


# Application definition #django 的自带应用
# APP列表
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'blacklist',
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 使用中文
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'automatic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'automatic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'terrace_db',
        'USER': 'root',
        'PASSWORD': '123456abc',
        'HOST': '192.168.0.54',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

#USE_TZ = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# 将静态资源存放在文件夹 static下
STATIC_URL = '/static/'

#STATIC_ROOT = '/static/'

# 设置根目录的静态资源文件夹 static
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

parse_sql_number = [10,50,200]

# LOG配置
BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 日志文件的格式
    'formatters': {
        # 详细的日志格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        # 简单的日志格式
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    # 处理器
    'handlers': {
        #打印SQL语句，方便开发
        'sql': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, "sql_info.log"),
             'maxBytes': 1024 * 1024 * 100,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        #在终端打印
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        # 默认的
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, "automatic.log"),
            'maxBytes': 1024 * 1024 * 100,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },

    'loggers': {
        # default日志
        'default': {
            'handlers': ['console', 'default'],
            'level': 'DEBUG'
        },
        #
        'django.db.backends': {
            'handlers': ['sql', 'console'],
            'propagate': True,
            'level': 'DEBUG',
        },

    }
}
