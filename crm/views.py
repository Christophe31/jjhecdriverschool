# -*- coding:utf8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
import datetime
from crm import forms
from common import models


@permission_required('view_customers')
def view_customers(request, other=None):
    return render(request, "crm/view_customers.html",
                  {
                      'customers': User.objects.all(),
                  })


@permission_required('view_customers')
def register_user(request):
    if request.POST:
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm.index')
    else:
        form = forms.UserForm()

    return render(request, "crm/register_user.html",
                  {
                      'form':form,
                  })


@permission_required('view_customers')
def billing(request, user_id=None, bill_id=None):
    customer = get_object_or_404(User, pk=user_id)
    if bill_id:
        instance = get_object_or_404(models.Transaction, id=bill_id)
    else:
        instance = None

    if request.POST:
        form = forms.BillingForm(request.POST, instance=instance,
                                 user=request.user, customer=customer)
        if form.is_valid():
            form.save()
            return redirect('crm.index')
    else:
        form = forms.BillingForm(user=request.user, customer=customer)

    return render(request, "crm/billing.html",
                  {
                      'customer': customer,
                      'form' : form
                  })


@permission_required('view_customers')
def add_score(request, user_id=None):
    customer = get_object_or_404(User, pk=user_id)
    if request.POST:
        form = forms.CodeMarkForm(request.POST, user=customer)
        if form.is_valid():
            form.save()
            return redirect('crm.index')
    else:
        form = forms.CodeMarkForm(user=customer)
    return render(request, "crm/add_score.html",
                  {
                      'form': form,
                      'customer': customer,
                  })


@permission_required('view_customers')
def register_formation(request, user_id=None):
    customer = get_object_or_404(User, pk=user_id)
    if request.POST:
        form = forms.DrivingLessonForm(request.POST, customer=customer)
        if form.is_valid():
            form.save()
            return redirect('crm.index')
    else:
        form = forms.DrivingLessonForm(customer=customer)
    return render(request, "crm/register_formation.html",
                  {
                      'customer': customer,
                      'form': form,
                  })



@permission_required('view_customers')
def register_exam(request, user_id=None):
    customer = get_object_or_404(User, pk=user_id)
    formations = models.Formation.objects.filter(transaction__in=customer.transactions_buyed.all())
    if request.POST:
        form = forms.ExamForm(request.POST)
        if form.is_valid():
            form.save(customer=customer)
            return redirect('crm.index')
    else:
        form = forms.ExamForm()
    return render(request, "crm/register_exam.html",
                  {
				      "form": form,
					  'formations':formations,
                      'customer': customer,
                  })

def ajax_get_exam(request):
    return HttpResponse(json.dumps(
	    [[exam.id, unicode(exam)] for exam in
			models.Exam.objects
			.filter(license__exact=request.GET['type'])
            .filter(start__gte=datetime.datetime.now())
			.filter(agence__exact=request.user.get_profile().place)
			#if exam.place_avail]
        ]
	))

