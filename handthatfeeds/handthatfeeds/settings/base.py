import os
from os.path import abspath, dirname

from django.core.exceptions import ImproperlyConfigured

ENV_VARIABLE_PREFIX = 'HANDTHATFEEDS'

def get_env_variable(var_name, optional=False):
    """Get the environment variable or return exception"""
    if not ENV_VARIABLE_PREFIX:
        raise ImproperlyConfigured('Set ENV_VARIABLE_PREFIX')
    try:
        return os.environ[ENV_VARIABLE_PREFIX + '_' + var_name]
    except KeyError:
        if optional:
            return None
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)


DATABASES = {
    'default': {
        # > createdb -T template_postgis livinglotsla
        # > psql
        # # create user livinglotsla with password 'password';
        # # grant all privileges on database livinglotsla to
        # livinglotsla;
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'HOST': get_env_variable('DB_HOST'),
        'PORT': get_env_variable('DB_PORT'),
    }
}

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('es', gettext('Spanish')),
)

LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True
TIME_ZONE = 'America/New_York'

PROJECT_ROOT = os.path.join(abspath(dirname(__file__)), '..', '..')

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collected_static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SECRET_KEY = get_env_variable('SECRET_KEY')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'honeypot.middleware.HoneypotMiddleware',
    'handthatfeeds.middleware.CrossSiteSharingMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',

    'feincms.context_processors.add_page_if_missing',
)

ROOT_URLCONF = 'handthatfeeds.urls'

WSGI_APPLICATION = 'handthatfeeds.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (

    #
    # django contrib
    #
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    #
    # third-party
    #
    'feincms',
    'feincms.module.medialibrary',
    'feincms.module.page',
    'honeypot',
    'rest_framework',

    #
    # Project-specific
    #
    'cms',
    'content',
    'organizations',

)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

#RECAPTCHA_PRIVATE_KEY = get_env_variable('RECAPTCHA_PRIVATE_KEY')
#RECAPTCHA_PUBLIC_KEY = get_env_variable('RECAPTCHA_PUBLIC_KEY')

EMAIL_SUBJECT_PREFIX = '[handthatfeeds] '

FEINCMS_RICHTEXT_INIT_TEMPLATE = 'admin/content/richtext/init_tinymce4.html'
FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': STATIC_URL + 'node_modules/tinymce/tinymce.min.js',
}

HONEYPOT_FIELD_NAME = 'homepage_url'
HONEYPOT_VALUE = 'http://example.com/'
