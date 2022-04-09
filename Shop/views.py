from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth import logout
from django.http import Http404
from .models import ExUser, Flower, Discount


def index(request):
    return render(request, 'home.html')


def catalog(request):
    all = Flower.objects.all()
    return render(request, 'catalog.html', {'flowers': all})


def card(request, articul: str):
    try:
        flower = Flower.objects.get(articul=articul)
    except Exception as e:
        print("OK")
        raise Http404("Flower does not exist")
    else:
        return render(request, 'card.html', {'flower': flower})
