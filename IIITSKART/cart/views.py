from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.http import *
from django.contrib.auth import *
from django.contrib.auth.models import User

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
        return render(request , 'cart/dashboard.html')


def login_page(request):
    return render(request, 'registration/login.html', {})


def profile_val(request):

    try:
        us = request.POST['username']
        paswd = request.POST['password']
        allusers = User.objects.all()
        for users in allusers:
            if users.username == us and users.password == paswd:
                return render(request, 'cart/dashboard.html')
    except:
        return render(request , 'cart/error-page.html')


def dashboard(request):

    return HttpResponseRedirect("/cart/index/")

def home(request):
    return render(request,'cart/landing.html')


def makeuser(request):
    if request.method == 'POST':
        try:
            if User.objects.filter(username=request.POST['email']).count() == 0:
                uobj = User()
                uobj.username=request.POST['username']
                uobj.first_name = request.POST['f_name']
                uobj.last_name = request.POST['l_name']
                uobj.email = request.POST['email']
                uobj.password = request.POST['password']
                uobj.save()
                return redirect( 'cart : dashboard', uobj.name)
            else:
                return render(request, 'cart/dashboard.html', {})
        except MultiValueDictKeyError:
            return render(request, 'cart/error-page.html', {})

# address = request.POST['address']
# inst = customer()
# inst.address = address
# inst.user = User.objects.get(username=request.user)
# int.save()
