#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import models as auth_models
from common import models


class UserForm(forms.ModelForm):

    class Meta:
        model = auth_models.User
        exclude = ("password", "is_staff", "is_active", "is_superuser",
                   "last_login", "date_joined", "groups", "user_permissions")

    username = forms.RegexField(label="Pseudonyme", max_length=30,
        regex=r'^[\w.@+-]+$', help_text = "Requiert 30 charactères ou moins."
        "Lettres, chiffres et @/./+/-/_ seulement.", error_messages = {
            'invalid': "Contient seulement lettres, nombres et @/./+/-/_ "
        })
    birth_date = forms.DateField()
    last_code_date = forms.DateField(widget=forms.DateInput(
                                        attrs={'readonly': True}))
    adress = forms.CharField()
    postal_code = forms.IntegerField(u"Code Postal")
    town = forms.CharField(u"Ville")
    phone_number = forms.RegexField(regex=r'\d{2}.\d{2}.\d{2}.\d{2}.\d{2}')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        if self.instance.id:
            prof = self.instance.get_profile()
            self.fields["birth_date"].initial = prof.birth_date
            self.fields["adress"].initial = prof.adress
            self.fields["postal_code"].initial = prof.postal_code
            self.fields["town"].initial = prof.town
            self.fields["phone_number"].initial = prof.phone_number

    def save(self, *args, **kwargs):
        usr = super(UserForm, self).save(*args, **kwargs)
        cd = self.cleaned_data
        prof = usr.get_profile()
        prof.birth_date = cd["birth_date"],
        prof.adress = cd["adress"],
        prof.postal_code = cd["postal_code"],
        prof.town = cd["town"],
        prof.phone_number = cd["phone_number"],
        prof.save()
        return usr
