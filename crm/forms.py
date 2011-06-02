#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from common import models

class TransactionSelling(forms.ModelForm):
    class Meta:
        model = models.Transaction
