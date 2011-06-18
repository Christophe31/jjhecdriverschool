#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('trainer.views',
    url('^$','mark_client', name='trainer.index'),
    url('^Booom\!$','declare_incident',name='trainer.declare_incident'),
    )
