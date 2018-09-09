"""iiitscart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include,path
from django.contrib import admin
from cart import views


urlpatterns = [
##   path('cart/', include('cart.urls')),
   path('admin/', admin.site.urls),
   path('', views.home, name='home'),
   path('index/', views.index, name='index'),
   path('auth/', include('social_django.urls', namespace='social')),
   path('accounts/', include('django.contrib.auth.urls')),
]
