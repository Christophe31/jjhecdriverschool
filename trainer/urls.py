#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('trainer.views',
    url('^(?:name/(?P<name>\S*))?$','greetings', name='intranet.greetings'))

# vim:set et sts=4 ts=4 tw=80:
