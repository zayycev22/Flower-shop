from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Shop.views import *
urlpatterns = [
    path('', index),
    path('catalog', catalog),
    path('home', index)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)