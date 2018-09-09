from django.urls import path
from django.urls import include,path

from . import views

urlpatterns = [

   path(r'^index/$', views.index, name='index'),
   path(r'^auth/$', include('social_django.urls', namespace='social')),
    
    
]
