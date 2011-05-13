#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from common import models as mod

class PackageInline(admin.TabularInline):
    model = mod.Package


class FormulaAdmin(admin.ModelAdmin):
    inlines = (PackageInline,)
    # défini les champs à afficher pour retirer Users
    # qui sera défini logiciellement depuis l'interface "faite main"
    fields = ("name","price")


admin.site.register(mod.Formula, FormulaAdmin)
admin.site.register(mod.Vehicule)
admin.site.register(mod.Event)
admin.site.register(mod.Place)
admin.site.register(mod.Formation)

# vim:set et sts=4 ts=4 tw=80:
