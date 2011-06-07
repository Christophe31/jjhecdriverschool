# -*- coding:utf8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from crm import forms
#from common import models


@permission_required('add_transaction')
def selling(request, customer=None, transaction=None):
    form = forms.TransactionSelling(request.POST or None, instance=transaction)
    if request.POST and form.isvalid():
        form.save()
    return render(request, "crm/selling.html", {"form": form})


@permission_required('view_customers')
def view_customers(request):
    return render(request, "crm/view_customers.html",
                  {
                      'customers': User.objects.all(),
                  }
                 )
