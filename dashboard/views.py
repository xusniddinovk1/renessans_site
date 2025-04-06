from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import forms
from . import services
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
    pictures = Fotogalereya.objects.all()
    oquvbolim = OquvBolim.objects.all()
    istirohatzona = IstirohatZona.objects.all()
    faoliyat = Faoliyat.objects.all()

    ctx = {
        "counts": {
            "pictures": len(pictures),
            "oquvbolim": len(oquvbolim),
            "istirohatzona": len(istirohatzona),
            "faoliyat": len(faoliyat),
        }
    }
    return render(request, "dashboard/index.html", ctx)


def gallery_create(request):
    model = Fotogalereya()
    form = forms.Fotot