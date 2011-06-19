from django.shortcuts import render, get_object_or_404
from trainer import forms
from common import models

def mark_client(request, id=None):

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
    return render(request, "trainer/declare_incident.html",
                 {
                        "form":form,
                 })
