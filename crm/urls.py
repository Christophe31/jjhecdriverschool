#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('crm.views',
    url('^$','selling', name='crm.index'))

# vim:set et sts=4 ts=4 tw=80:
