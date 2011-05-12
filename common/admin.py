#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from common import models as mod

class EventInline(admin.TabularInline):
    model = mod.Event


class FormationAdmin(admin.ModelAdmin):
    inlines = (EventInline,)


class PackageInline(admin.TabularInline):
    model = mod.Package


class FormulaAdmin(admin.ModelAdmin):
    inlines = (PackageInline,)


admin.site.register(mod.Formula, FormulaAdmin)
admin.site.register(mod.Vehicule)
admin.site.register(mod.Event)
admin.site.register(mod.Place)
admin.site.register(mod.Formation, FormationAdmin)

# vim:set et sts=4 ts=4 tw=80:
