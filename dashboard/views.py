from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import forms
from lager_app.forms import *
from lager_app.models import *


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


@login_required_decorator
def login_page(request):
    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_dashboard")
        return render(request, "dashboard/login.html")


def logout_page(request):
    logout(request)
    return redirect("login_page")


def main_dashboard(request):
    pictures = Gallery.objects.all()
    education = Education.objects.all()
    rest_area = RestArea.objects.all()
    activity = Activity.objects.all()

    ctx = {
        "counts": {
            "pictures": len(pictures),
            "education": len(education),
            "rest_area": len(rest_area),
            "activity": len(activity),
        }
    }
    return render(request, "dashboard/index.html", ctx)


def gallery_create(request):
    model = Gallery()
    form = Ga