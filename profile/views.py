from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def greetings(request, name=None):
    return render(request,
                  "profile/greetings.html",
                  {"name": name or "no_name",})

def login(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.POST and form.is_valid():
        auth_login(request, form.get_user())
        return redirect(request.GET.get('next','/'))
    return render(request,
                  "profile/login.html",
                  {"form": form,})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/')

# Create your views here.
