from django.shortcuts import render_to_response

def greetings(request, name=""):
    return render_to_response("intranet/greetings.html",{"name": name})

# Create your views here.
