"""
Django settings for marketplace project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from backend.core.utils import get_bool_from_env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^m1yh^j1xm1ut(1*=3ae3l$2ugv#d1dohxjm1e3z(odca*)tcf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_bool_from_env('DEBUG', False)

GRAPHQL_BATCH = True

ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_WEB_HOST', 'office.sngy.ru'),
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'backend.users.apps.UsersConfig',
    'backend.notifications.apps.NotificationsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'backend.core.middleware.isUserAuthenticatedMiddleware',
]

ROOT_URLCONF = 'backend.core.urls'

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

WSGI_APPLICATION = 'backend.core.wsgi.application'

GRAPHENE = {
    'SCHEMA': 'backend.core.api.schema',
    'MIDDLEWARE': [
        # 'crm.api.AuthorizationMiddleware'
    ]
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

db_host, db_port = os.environ.get('DB_HOST', 'localhost:5432').split(':')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'postgres'),
        'USER': os.environ.get('DB_USER', 'marketplace'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'marketplace'),
        'HOST': db_host,
        'PORT': db_port
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


# Logging
LOGGING = {}
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '[{levelname}][{asctime}][{module}][{funcName}]: {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '[{levelname}][{asctime}]: {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': './django.log',
#             'formatter': 'verbose',
#             'filters': ['require_file_log_true']
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'verbose',
#             'filters': ['require_debug_false']
#         },
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'require_file_log_true': {
#             '()': 'synergycrm.log.RequireFileLogTrue',
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'production': {
#             'handlers': ['console', 'file'],
#             'level': 'WARNING',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['mail_admins', 'console'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#     }
# }

ENABLE_FILE_LOG = os.environ.get('ENABLE_FILE_LOG', False)
ENABLE_DB_LOG = os.environ.get('ENABLE_DB_LOG', False)


AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Volgograd'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', '/var/www/ver2/static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/var/www/ver2/media/')

# Куки
SESSION_COOKIE_AGE = 3600 * 12  # Кука сессии живет 12 часов

