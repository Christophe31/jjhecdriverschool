#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('profile.views',
    url('^(?:name/(?P<name>\S*))?$', 'greetings', name='profile.index'),
    url('^login$', 'login', name='profile.login'),
    url('^logout$', 'logout', name='profile.logout'),
    url('bill/', 'bill', name='profile.bill'),
    url('edit_profile/', 'edit_profile', name='profile.edit_profile'),
    url('ajax_get_notes_range', 'ajax_get_notes_range', name='profile.ajax_get_notes_range'),
    url('ajax_get_notes_range/(?P<user>\d)', 'ajax_get_notes_range',
        name='profile.ajax_get_notes_range_for_user'),
    url('get_code_marks', 'get_code_marks', name='profile.get_code_marks'),
    url('get_driving_marks','get_driving_marks', name='profile.get_driving_marks'),
    url('ajax_get_appointments', 'ajax_get_appointments', name='profile.ajax_get_appointments'),
    url('get_appointments', 'get_appointments', name='profile.get_appointments')
)

# vim:set et sts=4 ts=4 tw=80:
