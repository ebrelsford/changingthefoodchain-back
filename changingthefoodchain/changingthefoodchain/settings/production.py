import os

from .base import *


ADMINS = (
    ('Eric', 'ebrelsford@gmail.com'),
)

MANAGERS = (
    ('Eric', 'ebrelsford@gmail.com'),
)

DJANGO_MODERATION_MODERATORS = (
    'ebrelsford@gmail.com',
)

ALLOWED_HOSTS = get_env_variable('ALLOWED_HOSTS').split(',')
BASE_URL = 'http://backend.changingthefoodchain.org'


#
# email
#
INSTALLED_APPS += (
    'mailer',
)
EMAIL_BACKEND = 'mailer.backend.DbBackend'
EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_HOST_USER = get_env_variable('EMAIL_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = get_env_variable('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = get_env_variable('SERVER_EMAIL')


#
# Caching
#
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:' + get_env_variable('MEMCACHED_SOCKET'),
    }
}


#
# CORS
#
CORS_ORIGIN_WHITELIST = (
    'changingthefoodchain.org',
)


#
# logging
#
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'log_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_ROOT, '../../logs', 'django.log'),
            'maxBytes': '16777216', # 16megabytes
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
    'root': {
        'handlers': ['log_file', 'mail_admins'],
        'level': 'WARNING',
    },
}


#
# SSL
#
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
