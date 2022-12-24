from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from .models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                print("Success in register")
                login(request, user)
                return redirect("dashboard")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        form = LoginForm(request.POST or None)
        context = {"form": form}
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                print("Error1")
        else:
            print("Error2")
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")
