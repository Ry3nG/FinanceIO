from django.shortcuts import render, redirect
from django.urls.resolvers import URLPattern
from django.template import loader

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('accounts:login')

