from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from dashboard import forms
from dashboard.forms import GalleryForm, EducationForm, ActivityForm, RestAreaForm
from lager_app.models import *


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_dashboard")
    return render(request, "dashboard/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required_decorator
def main_dashboard(request):
    galleries = Gallery.objects.all()
    educations = Education.objects.all()
    rest_areas = RestArea.objects.all()
    activities = Activity.objects.all()

    ctx = {
        "counts": {
            "galleries": len(galleries),
            "educations": len(educations),
            "rest_areas": len(rest_areas),
            "activities": len(activities),
        }
    }
    return render(request, "dashboard/index.html", ctx)


@login_required_decorator
def gallery_create(request):
    model = Gallery()
    form = forms.GalleryForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("gallery_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/gallery/form.html", ctx)


@login_required_decorator
def gallery_edit(request, pk):
    model = Gallery.objects.get(pk=pk)
    form = forms.GalleryForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("gallery_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/gallery/form.html", ctx)


@login_required_decorator
def gallery_delete(request, pk):
    model = Gallery.objects.get(pk=pk)
    model.delete()
    return redirect("gallery_list")


@login_required_decorator
def gallery_list(request):
    galleries = Gallery.objects.all()
    ctx = {
        "galleries": galleries
    }
    return render(request, "dashboard/gallery/list.html", ctx)


@login_required_decorator
def activity_create(request):
    model = Activity()
    form = forms.ActivityForm(request.POST or None, request.FILES,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("activity_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/activity/form.html", ctx)


@login_required_decorator
def activity_edit(request, pk):
    model = Activity.objects.get(pk=pk)
    form = forms.ActivityForm(request.POST or None, request.FILES,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("activity_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/activity/form.html", ctx)


@login_required_decorator
def activity_delete(request, pk):
    model = Activity.objects.get(pk=pk)
    model.delete()
    return redirect("activity_list")


@login_required_decorator
def activity_list(request):
    activities = Activity.objects.all()
    ctx = {
        "activities": activities
    }
    return render(request, "dashboard/activity/list.html", ctx)


@login_required_decorator
def education_create(request):
    model = Education()
    form = forms.EducationForm(request.POST or None, request.FILES,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("education_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/education/form.html", ctx)


@login_required_decorator
def education_edit(request, pk):
    model = Education.objects.get(pk=pk)
    form = EducationForm(request.POST or None, request.FILES,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("education_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/education/form.html", ctx)


@login_required_decorator
def education_delete(request, pk):
    model = Education.objects.get(pk=pk)
    model.delete()
    return redirect("education_list")


@login_required_decorator
def education_list(request):
    educations = Education.objects.all()
    ctx = {
        "educations": educations
    }
    return render(request, "dashboard/education/list.html", ctx)


@login_required_decorator
def rest_area_create(request):
    model = RestArea()
    form = forms.RestAreaForm(request.POST or None, request.FILES,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("rest_area_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/rest_area/form.html", ctx)


@login_required_decorator
def rest_area_edit(request, pk):
    model = RestArea.objects.get(pk=pk)
    form = RestAreaForm(request.POST or None, request.FILES,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("rest_area__list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/rest_area/form.html", ctx)


@login_required_decorator
def rest_area_delete(request, pk):
    model = RestArea.objects.get(pk=pk)
    model.delete()
    return redirect("rest_area_list")


@login_required_decorator
def rest_area_list(request):
    rest_areas = RestArea.objects.all()
    ctx = {
        "rest_areas": rest_areas
    }
    return render(request, "dashboard/rest_area/list.html", ctx)
