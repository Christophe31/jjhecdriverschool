Requirements
============
This list need to be kept up to date, if we use packages (ex: forum, blog)

Binary packages
---------------

Required:

 - Python 2.7
 - setuptools or distutils to deploy python requirments

Optionnal:

 - graphviz (to render database schemas)


python pakages
--------------

If you have installed python, you may want to use *"pip install <pakage>"* or
*"easy_install <package>"* to deploy folowing dependencies.

 - django
 - django-blog-zinnia
 - pil
 - lbforum
 - django-uni-form
 - django-tinymce

Optionnal (you may have to comments lines in settings.py if you don't want some features):

 - werkzeug (to use manage.py runserver_plus)
 - `django-extensions`_
 - django-debug-toolbar

: _`django-extensions` : http://packages.python.org/django-extensions/

Run the application
===================
To get a working database,

::

    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver

it will create a sqlite database "sqlite.db" in the root od your project
directory.

