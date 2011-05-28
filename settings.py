from os import path
basepath = path.abspath(path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Christophe Narbonne', 'test@example.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',                      # Or path if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost.
        'PORT': '',                      # Set to empty string for default.
    }
}

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'

SITE_ID = 1

INTERNAL_IPS = ('127.0.0.1',)

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = path.join(basepath, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = path.join(basepath,'static')
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2rz!4+4zbymz+rbppqlikpn*vxe1ym7=*vv*c^pfso+w=it5z8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'onlineuser.middleware.OnlineUserMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'zinnia.context_processors.media',
    'djangohelper.context_processors.ctx_config',
    'mobileadmin.context_processors.user_agent',
)

ROOT_URLCONF = 'jjhecdriverschool.urls'

TEMPLATE_DIRS = (
    path.join(basepath, 'templates'),
)

INSTALLED_APPS = (
    # django built in apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.comments',
    # dependences
    'mptt',
    'tagging',
    'zinnia',
    'tinymce',
    'uni_form',
    'django_extensions',
    'debug_toolbar',
    'pagination',
    'south',
    'lbforum',
    'simpleavatar',
    'djangohelper',
    'onlineuser',
    'attachments',
    'mobileadmin',
    'jqmobile',

    # local apps
    'jjhecdriverschool.hello_world',
    'jjhecdriverschool.crm',
    'jjhecdriverschool.trainer',
    'jjhecdriverschool.profile',
    'jjhecdriverschool.common',
)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

#AUTH_PROFILE_MODULE = 'common.UserProfile'
#AUTH_PROFILE_MODULE = 'lbforum.LBForumUserProfile'
ADMIN_MEDIA_PREFIX = '/static/admin/'
LOGIN_URL = '/profile/login/'
LOGOUT_URL = '/profile/logout/'
REGISTER_URL = '/profile/register/'
ZINNIA_AKISMET_COMMENT = False
LBFORUM_MEDIA_PREFIX = '%slbforum/' % MEDIA_URL

CTX_CONFIG = {
    'LBFORUM_TITLE': 'Safe Driving',
    'LBFORUM_SUB_TITLE': 'A forum engine written in Python using Django',
    'FORUM_PAGE_SIZE': 50,
    'TOPIC_PAGE_SIZE': 20,
    'LBFORUM_MEDIA_PREFIX': LBFORUM_MEDIA_PREFIX,
    'LOGIN_URL': LOGIN_URL,
    'LOGOUT_URL': LOGOUT_URL,
    'REGISTER_URL': REGISTER_URL,
}

BBCODE_AUTO_URLS = True
HTML_SAFE_TAGS = ['embed']


try:
        from local_settings import *
except ImportError:
        pass
