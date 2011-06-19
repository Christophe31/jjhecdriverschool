#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import models as auth_models
from common import models


class UserForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    birth_date = forms.DateField()
    last_code_date = forms.DateField()
    email = forms.EmailField()
    adress = forms.CharField()
    postal_code = forms.IntegerField(u"Code Postal")
    town = forms.CharField(u"Ville")
    phone_number = forms.RegexField(regex=r'\d{2}.\d{2}.\d{2}.\d{2}.\d{2}')

    def save(self):
        cd = self.cleaned_data
        usr = auth_models.User(
                    username=cd["username"],
                    first_name=cd["first_name"],
                    last_name=cd["last_name"],
                    email=cd["email"],
            )
        usr.set_password(cd["password"])
        usr.save()
        prof = models.UserProfile(
                    user=usr,
                    birth_date=cd["birth_date"],
                    last_code_date=cd["last_code_date"],
                    adress=cd["adress"],
                    postal_code=cd["postal_code"],
                    town=cd["town"],
                    phone_number=cd["phone_number"],
                    type=dict((v,k) for k,v in  models.UserProfile.TYPES)
                                                              ["Customer"]
            )
        prof.save()


class BillingForm(forms.ModelForm):

    class Meta:
        model = models.Transaction
        exclude = ('customer', 'seller')

    def __init__(self, *args, **kwargs):
        seller = kwargs.pop('user', None)
        customer = kwargs.pop('customer', None)
        super(BillingForm, self).__init__(*args, **kwargs)
        if (seller == None or customer == None):
            raise Exception("BillingForm nee a `user` and a `customer` argument")
        self.instance.seller = seller
        self.instance.customer = customer


class CodeMarkForm(forms.ModelForm):
    class Meta:
        model = models.CodeMark
        exclude=('user',)

    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('user', None)
        super(CodeMarkForm, self).__init__(*args,**kwargs)
        self.instance.user = customer


class TransactionSelling(forms.ModelForm):
    class Meta:
        model = models.Transaction


class ExamForm(forms.Form):
    type = forms.ChoiceField(choices=models.Exam.LICENCES,help_text="Le type d'examen")
    exam = forms.ChoiceField(help_text="Choix de l'examen pour l'inscription")


class DrivingLessonForm(forms.ModelForm):
    class Meta:
        model = models.Formation
        exclude = ('customer', 'comment', 'agence')
