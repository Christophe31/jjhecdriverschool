#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('profile.views',
    url('^(?:name/(?P<name>\S*))?$', 'greetings', name='profile.index'),
    url('^login$', 'login', name='profile.login'),
    url('^logout$', 'logout', name='profile.logout'),
)

# vim:set et sts=4 ts=4 tw=80:
