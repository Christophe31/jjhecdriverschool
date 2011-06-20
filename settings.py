#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

STATIC_ROOT = path.join(basepath, 'static')
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
if not hasattr(globals(), 'SECRET_KEY'):
    SECRET_FILE = path.join(basepath, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            import string
            symbols = ''.join((string.lowercase,
                               string.digits,
                               string.punctuation))
            SECRET_KEY = ''.join([choice(symbols) for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            raise Exception('Please create a %s file with random characters '
                            'to generate your secret key!' % SECRET_FILE)

# List of callables that know how to import templates from various sources.
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
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'djangobb_forum.middleware.LastLoginMiddleware',
    'djangobb_forum.middleware.UsersOnline',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'zinnia.context_processors.media',
    'django_authopenid.context_processors.authopenid',
    'djangobb_forum.context_processors.forum_settings',
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
    'django.contrib.flatpages',
    'flatpages_tinymce',
    'mptt',
    'tagging',
    'zinnia',
    'tinymce',
    'uni_form',
    'django_extensions',
    'debug_toolbar',
    'south',
    'registration',
    'django_authopenid',
    'messages',
    'djangobb_forum',
    'haystack',
    'mobileadmin',
    'jqmobile',

    # local apps
    'jjhecdriverschool.home',
    'jjhecdriverschool.crm',
    'jjhecdriverschool.trainer',
    'jjhecdriverschool.profile',
    'jjhecdriverschool.common',
)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

AUTH_PROFILE_MODULE = 'common.UserProfile'
#AUTH_PROFILE_MODULE = 'lbforum.LBForumUserProfile'
ADMIN_MEDIA_PREFIX = '/static/admin/'
LOGIN_URL = '/profile/login/'
LOGOUT_URL = '/profile/logout/'
REGISTER_URL = '/profile/register/'
ZINNIA_AKISMET_COMMENT = False

# Haystack settings
HAYSTACK_SITECONF = 'search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = path.join(basepath, 'djangobb_index')

# Account settings
ACCOUNT_ACTIVATION_DAYS = 10
LOGIN_REDIRECT_URL = '/forum/'
LOGIN_URL = '/profile/login'

#Cache settings
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

try:
        from local_settings import *
except ImportError:
        pass
