#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from common import models


class MarkCustommerForm(forms.ModelForm):
    class Meta:
        model = models.Formation
        exclude = ("agence", "vehicule", "package", "trainer", "transaction")


class DeclareIncidentForm(forms.ModelForm):
    class Meta:
        model = models.Maintenance
