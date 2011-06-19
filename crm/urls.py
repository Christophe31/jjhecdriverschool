#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('crm.views',
    url('^$','view_customers', name='crm.index'),
    url('^list_customers$', 'view_customers', name='crm.view_customers'),
    url('^ajax_get_exam$', 'ajax_get_exam', name='crm.ajax_get_exam'),
    url('^register_user/new$', 'register_user', name='crm.register_user'),
    url('^billing/user/(?P<user_id>\d+)$', 'billing', name='crm.billing'),
    url('^add_score/user/(?P<user_id>\d+)$', 'add_score', name='crm.add_score'),
    url('^register_formation/user/(?P<user_id>\d+)$', 'register_formation', name='crm.register_formation'),
    url('^register_exam/user/(?P<user_id>\d+)$', 'register_exam', name='crm.register_exam'),
)
