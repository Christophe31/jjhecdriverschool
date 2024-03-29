#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from common import models as mod
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UserProfileInline(admin.StackedInline):
    model = mod.UserProfile


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline,)


class PackageInline(admin.TabularInline):
    model = mod.Package


class FormulaAdmin(admin.ModelAdmin):
    inlines = (PackageInline,)
    fields = ("name","price")


class ExamAdmin(admin.ModelAdmin):
    exclude = ("subscribers",)


class MarkFormation(mod.Formation):
    class Meta:
        proxy = True


class MarkFormationAdmin(admin.ModelAdmin):
    exclude = ("agence", "vehicule", "package", "trainer", "transaction")

# Reecrit l'interface des utilisateurs dans l'admin avec nos
# champs complementaires
admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

admin.site.register(mod.Formula, FormulaAdmin)
admin.site.register(mod.Vehicule)
admin.site.register(mod.Maintenance)
admin.site.register(mod.Place)
admin.site.register(mod.Formation)
admin.site.register(MarkFormation, MarkFormationAdmin)
admin.site.register(mod.CodeMark)
admin.site.register(mod.Exam, ExamAdmin)
admin.site.register(mod.Transaction)
