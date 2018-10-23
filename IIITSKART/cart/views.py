from django.core import serializers
from django.db import transaction
from django.core.files.storage import FileSystemStorage
from django.http import *
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import requests
import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import customer, c_review, p_review, Product, category
from .serializers import CustomerSerializer, C_reviewSerializer, P_reviewSerializer, ProductSerializer, \
    CategorySerializer


# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = CustomerSerializer


class C_reviewViewSet(viewsets.ModelViewSet):
    queryset = c_review.objects.all()
    serializer_class = C_reviewSerializer


class P_reviewViewSet(viewsets.ModelViewSet):
    queryset = p_review.objects.all()
    serializer_class = P_reviewSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#
# class LoginViewSet(viewsets.ModelViewSet):
#     queryset = login.objects.all()
#     serializer_class =  LoginSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializer


# class Super_UserViewSet(viewsets.ModelViewSet):
#     queryset = super_user.objects.all()
#     serializer_class =  Super_UserSerializer


def home(request):
    return render(request, 'cart/landing.html')


def sign_up(request):
    return render(request, 'cart/landing.html')


def dashboard(request):
    return render(request, 'cart/dashboard.html')


def login_page(request):
    return render(request, 'cart/landing.html', {})


def logout_view(request):
    logout(request)
    return render(request, 'cart/landing.html', {})


def search(request):
    return render(request, 'cart/search.html', {})


def add_pro(request):
    return render(request, 'cart/addproduct.html', {})


def profile_view(request):
    if request.user.is_authenticated:
        c_obj = customer()
        # temp= customer.objects.raw('SELECT * FROM cart_customer')
        # data = serializers.serialize('json', temp)
        # value=json.loads(data)
        # print(value["fields"])
        #
        #
        # c_user = request.user.username
        # print(c_user)
        #
        # cobj=customer()
        # cobj.phone=request.POST.get('phone', "")
        # cobj.address=request.POST.get('address', "")
        # cobj.blacklist=request.POST.get('blacklist', "")
    return render(request, 'cart/profile.html', {})


def go_to_dashboard(request):
    try:
        return render(request, 'cart/dashboard.html', {})
    except:
        pass


def profile_val(request):
    try:
        us = request.POST['username']
        pt = request.POST['password']
        user = authenticate(username=us, password=pt)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('cart:go-to-dashboard'))
        return render(request, 'cart/landing.html', {'error': 'Invalid email-id or password', })

    except:
        return render(request, 'cart/error-page.html', {})


def makeuser(request):
    if request.method == 'POST':
        print("in make user")
        print("in try")
        if User.objects.filter(username=request.POST.get('email', "")).count() == 0:
            uobj = User()
            uobj.username = request.POST.get('username', "")
            uobj.first_name = request.POST.get('first_name', "")
            uobj.last_name = request.POST.get('last_name', "")
            uobj.email = request.POST.get('email', "")
            # uobj.customer.avatar =
            uobj.set_password(request.POST.get('password', ""))
            # uobj.customer.phone =
            uobj.save()

            user = authenticate(username=uobj.username, password=request.POST.get('password', ""))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('cart:go-to-dashboard'))
        else:
            print("else")
            return render(request, '', {})


def profile_photo_upload(request):
    if request.method == 'POST' and request.FILES['avatar']:
        avatar = request.FILES['avatar']
        fs = FileSystemStorage()
        filename = fs.save(avatar.name, avatar)
        uploaded_file_url = fs.url(filename)
        print(filename)

        print(uploaded_file_url)

        cins = User.objects.get(username=request.user.username)
        cins.customer.avatar = filename
        cins.save()
        print(uploaded_file_url)
        return render(request, 'cart/profile.html', {'uploaded_file_url': uploaded_file_url})

    return render(request, 'cart/profile.html')
################ functions ############


def profile_data(request):
    temp = User.objects.raw('SELECT * FROM  auth_user')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    print(value[0]["fields"])

    # c_user = request.user.username
    # print(c_user)
    return HttpResponse("profile updated")


def add_product(request):
    if request.user.is_authenticated:
        uobj=User.objects.get(username=request.user.username)
        cobj = customer.objects.get(pk=uobj.customer.id)
        pro=cobj.product_set.create(title=request.POST.get("title"), quantity = request.POST.get("quantity"),
                                    description = request.POST.get("description"), price = request.POST.get("price"))

        catobj=category.objects.get(name=request.POST.get("cat_name"))
        print(catobj.id,pro.p_id)
        pro.cat_id=catobj
        pro.save()
        # pro1.cat_id=catobj.id
        return HttpResponse("added product")



        return HttpResponse("added product")


@transaction.atomic
def update_profile(request):
    # user = User.objects.get(pk=user_id)
    # user.profile.bio = 'lul'
    # user.save()
    return render(request, 'cart/dashboard.html')


@csrf_exempt
def profile_val_api(request):
    if request.method == 'POST':
        cust = json.loads(request.body)
        print(cust)
        us = cust['username']
        pt = cust['password']
        print(us)
        print(pt)
        user = authenticate(username=us, password=pt)
        if user is not None:
            return JsonResponse({"status": "Yes"})
    return JsonResponse({"status": "No"})


@csrf_exempt
def receive(request):
    if request.method == 'POST':

        cust = json.loads(request.body)
        obj = customer(first_name=cust['first_name'], last_name=cust['last_name'], address=cust['address'],
                       email=cust['email'], phone=cust['phone'], blacklist=cust['blacklist'])
        obj.save()
        print(cust['first_name'])

        return JsonResponse({"status": "post"})
    else:
        print('get req')
        return JsonResponse({"status": "get"})


def test(request):
    temp=customer.objects.raw('SELECT cart_customer.id FROM cart_customer inner join auth_user on cart_customer.user_id = auth_user.id and auth_user.username="chinmay"')
    # temp = customer.objects.raw('SELECT * FROM cart_customer')
    data=serializers.serialize('json',temp)
    value=json.loads(data)

    print(value)
    # print("sdfsdf")
    return  HttpResponse('TET')


@csrf_exempt
def receiveProduct(request):
    if request.method == 'POST':
        prod = json.loads(request.body)
        temp = category.objects.raw('SELECT * FROM cart_category')
        data = serializers.serialize('json', temp)
        value = json.loads(data)

        print(prod['quantity'])

        for i in range(len(value)):
            if value[i]['fields']['name']== prod['category']:
                cid=int(value[i]['pk'])


        temp = customer.objects.raw('SELECT cart_customer.id FROM cart_customer inner join auth_user on cart_customer.user_id = auth_user.id and auth_user.username="chinmay"')
        data = serializers.serialize('json', temp)
        value = json.loads(data)
        pid = value[0]['pk']

        pro_obj = Product(title=prod['title'], quantity=prod['quantity'], description=prod['description'],price=prod['price'], c_id=cid,p_id=pid)

        pro_obj.save()
        return JsonResponse({"status": "post"})
    else:
        print('get req')
        return JsonResponse({"status": "get"})


@csrf_exempt
def send(request):
    if request.method == 'GET':
        class_name = request.GET.get('class_name')
        print(class_name)
        if (class_name == 'Customer'):
            obj = customer.objects.all()
        if (class_name == 'C_Review'):
            obj = c_review.objects.all()
        if (class_name == 'Product'):
            obj = Product.objects.all()
        if (class_name == 'P_Review'):
            obj = p_review.objects.all()
        if (class_name == 'Category'):
            obj = category.objects.all()

        data = serializers.serialize('json', obj)
        jsonResponse = {
            'data': json.loads(data)
        }
        return JsonResponse(jsonResponse)
    else:
        print('Post request')
        jsonResponse = {
            'data': []
        }
        return JsonResponse(jsonResponse)
