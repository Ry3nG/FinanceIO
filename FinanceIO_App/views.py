from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q, Sum

from .models import TransactionInfo

from django.http import HttpResponseRedirect

# Create your views here.


def dashboard(request):
    budget_default = 1000
    expense_items = TransactionInfo.objects.filter(user_expense=request.user).order_by(
        "-date"
    )
    budget_total = TransactionInfo.objects.filter(user_expense=request.user).aggregate(
        budget=Sum("cost")
    )
    # set a default value for budget_total
    if budget_total["budget"] is None:
        budget_total["budget"] = budget_default

    expense_total = TransactionInfo.objects.filter(user_expense=request.user).aggregate(
        expenses=Sum("cost")
    )

    # set a default value for expense_total
    if expense_total["expenses"] is None:
        expense_total["expenses"] = 0

    budget_display = budget_default - expense_total["expenses"]
    context = {
        "expense_items": expense_items,
        "budget": budget_display,
        "expense": expense_total["expenses"],
    }
    return render(request, "dashboard.html", context)



def add_transaction(request):
    item_name = request.POST["item_name"]
    expense_cost = float(request.POST["cost"])
    transaction_date = request.POST["date"]
    # make sure that all expenses have a negative cost value
    TransactionInfo.objects.create(
        name=item_name, cost=expense_cost, date=transaction_date, user_expense=request.user
    )
    return redirect("dashboard")



def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
