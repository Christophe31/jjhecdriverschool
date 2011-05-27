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

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = path.join(basepath, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2rz!4+4zbymz+rbppqlikpn*vxe1ym7=*vv*c^pfso+w=it5z8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.eggs.Loader',
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
    'django.core.context_processors.media',
    'zinnia.context_processors.version',  # Optional
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


#from mobileadmin.conf import settings as settings

#mobileadmin_media_path = settings.MEDIA_PATH
#mobileadmin_media_prefix = settings.MEDIA_PREFIX

try:
        from local_settings import *
except ImportError:
        pass
