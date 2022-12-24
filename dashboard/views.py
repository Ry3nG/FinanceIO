from django.shortcuts import render, redirect
from django.urls.resolvers import URLPattern

def dashboard(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, "dashboard.html", {"message: Success!"})

