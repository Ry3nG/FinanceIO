from django.shortcuts import render, redirect
from django.urls.resolvers import URLPattern
from django.template import loader

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    else:
        template = loader.get_template("dashboard.html")
    return render(request, "dashboard.html")

