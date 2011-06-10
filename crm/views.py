# -*- coding:utf8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from crm import forms
from common import models


@permission_required('add_transaction')
def selling(request, customer=None, transaction=None):
    form = forms.TransactionSelling(request.POST or None, instance=transaction)
    if request.POST and form.isvalid():
        form.save()
    return render(request, "crm/selling.html", {"form": form})


@permission_required('view_customers')
def view_customers(request, other=None):
    return render(request, "crm/view_customers.html",
                  {
                      'customers': User.objects.all(),
                  })


@permission_required('view_customers')
def register_user(request):
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
        if form.isvalid():
            form.save()
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
    return render(request, "crm/add_score.html",
                  {
                      'customer': customer,
                  })


@permission_required('view_customers')
def register_formation(request, user_id=None):
    customer = get_object_or_404(User, pk=user_id)
    return render(request, "crm/register_formation.html",
                  {
                      'customer': customer,
                  })


@permission_required('view_customers')
def register_exam(request, user_id=None):
    customer = get_object_or_404(User, pk=user_id)
    return render(request, "crm/register_exam.html",
                  {
                      'customer': customer,
                  })
