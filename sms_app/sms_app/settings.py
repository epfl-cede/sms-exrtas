"""
Django settings for sms_app project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p@p8ac&7&5)v&=lv1(62#l)!6i7oko9lgtf-0nopdghhn3^njp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'split_logs.apps.SplitLogsConfig',
    'check_ssl.apps.CheckSslConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'sms_app.urls'

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

WSGI_APPLICATION = 'sms_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    },
    'edxapp_readonly': {
        'NAME': 'edxapp',
        'ENGINE': 'django.db.backends.mysql',
        'USER': os.environ.get('EDXAPP_MYSQL_USER', ''),
        'PASSWORD': os.environ.get('EDXAPP_MYSQL_PASSWORD', ''),
        'HOST': os.environ.get('EDXAPP_MYSQL_HOST', ''),
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/utils/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '[%(asctime)s] %(name)-12s %(levelname)-8s %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        # Redefining the logger for the `django` module
        # prevents invoking the `AdminEmailHandler`
        'django': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        #'split_logs.utils': {
        #    'handlers': ['console'],
        #    'level': 'DEBUG',
        #},
    }
}

TRACKING_LOGS_ORIGINAL_SRC=os.environ.get("TRACKING_LOGS_ORIGINAL_SRC")
TRACKING_LOGS_ORIGINAL_DST=os.environ.get("TRACKING_LOGS_ORIGINAL_DST")
TRACKING_LOGS_SPLITTED=os.environ.get("TRACKING_LOGS_SPLITTED")
TRACKING_LOGS_ENCRYPTED=os.environ.get("TRACKING_LOGS_ENCRYPTED")
DUMP_DB_PATH=os.environ.get("DUMP_DB_PATH")
DUMP_XML_PATH=os.environ.get("DUMP_XML_PATH")

SMS_APP_ENV=os.environ.get("SMS_APP_ENV")

AWS_STORAGE_BUCKET_NAME_ANALYTICS='{env}-analytics'.format(env=SMS_APP_ENV)

EDXAPP_MYSQL_HOST=os.environ.get("EDXAPP_MYSQL_HOST")
EDXAPP_MYSQL_USER=os.environ.get("EDXAPP_MYSQL_USER")
EDXAPP_MYSQL_PASSWORD=os.environ.get("EDXAPP_MYSQL_PASSWORD")

EMAIL_FROM_ADDRESS = 'noreply@epfl.ch'
EMAIL_TO_ADDRESSES = ['edx-monitor@groupes.epfl.ch']
