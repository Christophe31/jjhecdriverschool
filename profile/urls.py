#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('profile.views',
    url('^(?:name/(?P<name>\S*))?$','greetings', name='profile.index'))

# vim:set et sts=4 ts=4 tw=80:
