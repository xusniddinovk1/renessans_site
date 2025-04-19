from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import *
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
    form = forms.GalleryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("gallery_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/gallery/form.html", ctx)


def gallery_edit(request, pk):
    model = Gallery.objects.get(pk=pk)
    form = forms.GalleryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("gallery_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/gallery/form.html", ctx)


def gallery_delete(request, pk):
    model = Gallery.objects.get(pk=pk)
    model.delete()
    return redirect("gallery_list")

def gallery_list(request):
    galleries = Gallery.objects.all()
    ctx = {
        "galleries": galleries
    }
    return render(request, "dashboard/gallery/list.html", ctx)

def activity_create(request):
    model = Activity()
    form = forms.ActivityForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("activity_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/activity/form.html", ctx)


def activity_edit(request, pk):
    model = Activity.objects.get(pk=pk)
    form = forms.ActivityForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("activity_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/activity/form.html", ctx)


def activity_delete(request, pk):
    model = Activity.objects.get(pk=pk)
    model.delete()
    return redirect("activity_list")


def activity_list(request):
    activities = Activity.objects.all()
    ctx = {
        "activities": activities
    }
    return render(request, "dashboard/activity/list.html", ctx)


def education_create(request):
    model = Education()
    form = forms.EducationForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("education_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/education/form.html", ctx)


def education_edit(request, pk):
    model = Education.objects.get(pk=pk)
    form = EducationForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("education_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/education/form.html", ctx)


def education_delete(request, pk):
    model = Education.objects.get(pk=pk)
    model.delete()
    return redirect("education_list")


def education_list(request):
    educations = Education.objects.all()
    ctx = {
        "educations": educations
    }
    return render(request, "dashboard/education/list.html", ctx)

def rest_area_create(request):
    model = RestArea()
    form = forms.RestAreaForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("rest_area_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/rest_area/form.html", ctx)


def rest_area_edit(request, pk):
    model = RestArea.objects.get(pk=pk)
    form = RestAreaForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("rest_area__list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/rest_area/form.html", ctx)


def rest_area_delete(request, pk):
    model = RestArea.objects.get(pk=pk)
    model.delete()
    return redirect("rest_area_list")


# def rest_area_list(request):
#     rest_areas = RestArea.objects.all()
#     ctx = {
#         "rest_areas": rest_areas
#     }
#     return render(request, "dashboard/rest_area/list.html", ctx)
