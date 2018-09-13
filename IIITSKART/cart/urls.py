from django.urls import path

from . import views
app_name = 'cart'
urlpatterns = [
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
]