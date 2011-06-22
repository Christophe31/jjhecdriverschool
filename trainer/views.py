from django.shortcuts import render, get_object_or_404
from trainer import forms
from common import models
import datetime


def mark_client(request, id=None):
    if not id:
        id = iter(models.Formation.objects
                .filter(trainer__exact=request.user)
                .filter(start__lt=datetime.datetime.now())
                .order_by('-start')).next().id
    if request.POST:
        form = forms.MarkCustommerForm(request.POST, instance=get_object_or_404(models.CodeMark, pk=id))
        if form.is_valid():
            form.save()
    else:
        form = forms.MarkCustommerForm(instance=get_object_or_404(models.CodeMark, pk=id))
    return render(
            request,
            "trainer/mark_client.html",
            {
                "form": form,
            }
        )


def view_vehicles(request):
    qs = models.Vehicule.objects.filter(agence__exact=request.user.get_profile().place)
    return render(request,
                  "trainer/view_vehicles.html",
                  {
                      'vehicles': qs,
                  }
            )


def declare_incident(request, id):
    form = forms.DeclareIncidentForm(instance=get_object_or_404(models.Maintenance, pk=id))
    return render(request,
                  "trainer/declare_incident.html",
                 {
                        "form":form,
                 }
            )
