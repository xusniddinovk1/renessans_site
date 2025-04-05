from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import forms
from . import services


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


@login_required_decorator