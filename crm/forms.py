#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import models as auth_models
from common import models


class TransactionSellingForm(forms.ModelForm):

    class Meta:
        model = models.Transaction


class UserForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        import pdb;pdb.set_trace()
        auth_models.User


class BillingForm(forms.ModelForm):

    class Meta:
        model = models.Transaction
        exclude = ('customer','seller')

    def __init__(self, *args, **kwargs):
        seller = kwargs.pop('user', None)
        customer = kwargs.pop('customer', None)
        super(BillingForm, self).__init__(*args, **kwargs)
        if (seller == None or customer == None):
            raise Exception("BillingForm nee a `user` and a `customer` argument")
        self.instance.seller = seller
        self.instance.customer = customer

    def save(self, *args, **kwargs):
        super(BillingForm, self).save(*args, **kwargs)



class TransactionSelling(forms.ModelForm):
    class Meta:
        model = models.Transaction


class TransactionSelling(forms.ModelForm):
    class Meta:
        model = models.Transaction
