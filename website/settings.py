"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from email.utils import getaddresses
from typing import cast

import environ


env = environ.Env()
env.read_env('.env')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Application configuration

SECRET_KEY = env.str('SECRET_KEY', default='my-random-secret-key')

DEBUG = cast(bool, env.bool('DEBUG', default=False))

ALLOWED_HOSTS = env.list('HOSTS', default=[])

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # Our apps
    'users',
    'main',
    'heart',
    'blog',
    'clubs',
    'trading',
    'feedback',
    'sanalberto',
    'bot',

    # 3rd party
    'pagedown',
    'markdown_deux',
    'meta',
    'django_cleanup',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

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

WSGI_APPLICATION = 'website.wsgi.application'


# Database

DATABASES = {
    'default': env.db('DB_URL', default='sqlite:///db.sqlite3'),
}


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'propagate': True,
        }
    }
}


# Communication

ADMINS = getaddresses(cast(list, env.list('ADMINS', default=[])))

DEFAULT_FROM_EMAIL = env.str('EMAIL_FROM', default='DAFI <dafi@um.es>')

if not DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    EMAIL_USE_SSL = True

    EMAIL_CONFIG = env.email_url('EMAIL')
    vars().update(EMAIL_CONFIG)


# Auth

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

AUTH_USER_MODEL = 'users.User'

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'profile'


# Security

CSRF_COOKIE_SECURE = not DEBUG

SESSION_COOKIE_SECURE = not DEBUG

INTERNAL_IPS = [
    '127.0.0.1',
]


# Django Debug Toolbar

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
]


# Bot

BOT_TOKEN = env.str('BOT_TOKEN', default='')


# Payments

STRIPE_PK = env.str('STRIPE_PK', default='')

STRIPE_SK = env.str('STRIPE_SK', default='')


# FIUMCRAFT

FIUMCRAFT_WHITELIST_ENDPOINT = env.str('FIUMCRAFT_WHITELIST_ENDPOINT', default='')

FIUMCRAFT_WHITELIST_TOKEN = env.str('FIUMCRAFT_WHITELIST_TOKEN', default='')


# Internationalization

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Files

FILE_UPLOAD_PERMISSIONS = 0o644

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Metadata

META_SITE_NAME = 'DAFI'

META_SITE_PROTOCOL = 'http' if DEBUG else 'https'

META_USE_TITLE_TAG = True

META_USE_OG_PROPERTIES = True

META_USE_TWITTER_PROPERTIES = True

META_USE_SITES = True
