from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'rental'

urlpatterns = [
    path(r'rental/', views.rent, name='dashboard'),

    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

