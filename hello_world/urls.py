#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('hello_world.views',
    # regex python:
    # ^ debut, $ fin
    # \S caracteres non blancs (espaces, tab)
    # \d pour les numeriques.
    # (regex) zone de l'url a renvoyer a la vue
    # (?:regex) zone isolee non transmise a la vue pour y appliquer
    #               un repetiteur (ici ? pour dire 0 ou 1)
    # (?P<arg_name>regex) permet de nommer le paramettre dans la regex.
    url('^(?:name/(?P<name>\S*))?$','greetings', name='hello_world.index'))

# vim:set et sts=4 ts=4 tw=80:
