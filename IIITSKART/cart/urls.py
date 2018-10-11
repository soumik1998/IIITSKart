from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
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
    url(r'^',include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login-view/', views.login_page , name='login_page'),
    path('profilevalidation/',views.profile_val , name = 'profile_val'),
    path('makeuser/', views.makeuser, name='makeuser'),
    path(r'receive/', views.receive, name='receive'),
    path(r'send/', views.send, name='send')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)