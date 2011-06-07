#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('crm.views',
    url('^$','selling', name='crm.index'),
    url('^list_customers$', 'view_customers', name='crm.view_customers'),
    url('^billing/user/\d$', 'billing', name='crm.billing'),
    url('^add_score/user/\d$', 'add_score', name='crm.add_score'),
    url('^register_formation/user/\d$', 'register_formation', name='crm.register_formation'),
    url('^register_exam/user/\d$', 'register_exam', name='crm.register_exam'),
)
