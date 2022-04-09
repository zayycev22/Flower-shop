from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Shop.views import *
urlpatterns = [
    path('', index),
    path('catalog', catalog, name='catalog1'),
    path('home', index, name='home'),
    path('flower/<str:articul>', card, name='flower'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)