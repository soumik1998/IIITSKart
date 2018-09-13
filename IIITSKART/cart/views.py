from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.http import *
from django.contrib.auth import logout
import requests

from django.shortcuts import render
from rest_framework import viewsets
from .models import customer,c_review,p_review,product,login,category,super_user
from .serializers import CustomerSerializer,C_reviewSerializer,P_reviewSerializer,ProductSerializer,LoginSerializer,CategorySerializer,Super_UserSerializer
# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = customer.objects.all()
    serializer_class =  CustomerSerializer


class C_reviewViewSet(viewsets.ModelViewSet):
    queryset = c_review.objects.all()
    serializer_class =  C_reviewSerializer



class P_reviewViewSet(viewsets.ModelViewSet):
    queryset = p_review.objects.all()
    serializer_class =  P_reviewSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class =  ProductSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = login.objects.all()
    serializer_class =  LoginSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class =  CategorySerializer


class Super_UserViewSet(viewsets.ModelViewSet):
    queryset = super_user.objects.all()
    serializer_class =  Super_UserSerializer


def index(request):
    if request.user.is_authenticated: 
        return JsonResponse({
            'user': model_to_dict(request.user),
        }, safe=False)
    else:
        return HttpResponse('user not active')


def sign_up(request):
    return render(request, 'registration/signup.html')

def lout(request):
    logout(request)
    return  HttpResponse("you are logged out")

def loin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/cart/dashboard/")
         
    else:   
        return  HttpResponse("you are already  logged in") 


def dashboard(request):
    return HttpResponseRedirect("/cart/index/")

