from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth import logout
from django.http import Http404
from .models import ExUser, Flower, Discount


def set_new_user():
    try:
        a = ExUser(email="abcd@mail.com", password="123")
        a.save()
    except Exception as e:
        print(str(e))


def index(request):
    a = ExUser.objects.all()
    return render(request, 'index.html')
