from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers

from . import views
app_name = 'cart'
router = routers.DefaultRouter(views.CustomerViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'p_review', views.P_reviewViewSet)
router.register(r'C_review', views.C_reviewViewSet)

urlpatterns = [
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    url(r'^',include(router.urls))
]