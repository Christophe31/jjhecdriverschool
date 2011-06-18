#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from django.utils import simplejson as json
from profile import forms
import datetime
import time
from common import models


def greetings(request, name=None):
    return render(request,
                  "profile/greetings.html",
                  {"name": name or "no_name"})


def edit_profile(request):
    if request.POST:
        form = forms.UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile.index')
    else:
        form = forms.UserForm(instance=request.user)
    return render(request,"profile/edit_profile.html",{"form": form})


def login(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.POST and form.is_valid():
        auth_login(request, form.get_user())
        return redirect(request.GET.get('next', '/'))
    return render(request,
                  "profile/login.html",
                  {"form": form})


@csrf_exempt
def ajax_get_notes_range(request, start=None, end=False):
    qs = request.user.codemark_set.all()
    if start:
        try:
            qs.filter(date__gt=datetime.datetime.fromtimestamp(
                                int(float(start))))
        except:
            raise Http404()
    if end:
        try:
            qs.filter(date__lt=datetime.datetime.fromtimestamp(
                                int(float(end))))
        except:
            raise Http404()
    return HttpResponse(json.dumps(
            [[int(time.mktime(e.date.timetuple())), e.mark]
                                for e in request.user.codemark_set.all()]
        ))


def get_code_marks(request):
    return render(request, "profile/get_code_marks.html",{})


def get_driving_marks(request):
    formations = models.Formation.objects.filter(transaction__in=request.user.transactions_buyed.all())
    return render(request, "profile/get_driving_marks.html",{
        "formations": formations
    })


def get_appointments(request):
    return render(request, "profile/get_appointments.html",
                 {})


def ajax_get_appointments(request):
    return HttpResponse(json.dumps([
            {"id":event.id,
             "start":event.start.isoformat(),
             "end":event.end.isoformat(),
             "title": event.title
            }
            for event in models.Event.objects.all()
        ]))


@login_required
def logout(request):
    auth_logout(request)
    return redirect('/')


@login_required
def bill(request, user=None):
    if user == None:
        user = request.user
    else:
        pass
        # request.user.has_perm("")
    transactions = (models.Transaction.objects
                       .filter(customer=user.id)
                       .select_related('customer', 'seller', 'formula'))
    return render(request,
                  "profile/bill.html",
                  {
                      "transactions": transactions,
                  })

def appreciation(request):
    return render(request,
                  "profile/appreciations.html",
                  {
                      
                  })