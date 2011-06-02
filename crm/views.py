from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from crm import forms


@permission_required('add_transaction')
def selling(request, customer=None, transaction=None):
    form = forms.TransactionSelling(request.POST or None, instance=transaction)
    if request.POST and form.isvalid():
        form.save()
    return render(request, "crm/selling.html", {"form": form})
