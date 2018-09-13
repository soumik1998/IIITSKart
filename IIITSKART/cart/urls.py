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
router.register(r'Category', views.CategoryViewSet)
router.register(r'Superuser',views.Super_UserViewSet)
router.register(r'Login',views.LoginViewSet)

urlpatterns = [
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    url(r'^',include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login-view/', views.login_page , name='login_page'),
    path('profilevalidation/',views.profile_val , name = 'profile_val'),
    path('makeuser/', views.makeuser, name='makeuser'),
]