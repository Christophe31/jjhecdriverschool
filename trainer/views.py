from django.shortcuts import render, get_object_or_404
from trainer import forms


def mark_client(request, id=None):
    form = forms.MarkCustommerFrom(instance=get_object_or_404(pk=id))
    return render(
            request,
            "trainer/mark_client.html",
            {
                "form": form,
            }
        )


def declare_incident(request, id=None):
    form = forms.DeclareIncidentForm(instance=get_object_or_404(pk=id))
    return render(request, "trainer/declare_incident.html",
                 {
                        "form":form
                 })
