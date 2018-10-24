from django.core import serializers
from django.db import transaction
from django.core.files.storage import FileSystemStorage, default_storage
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
from .models import customer, c_review, p_review, Product, category,Order
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


def go_to_dashboard(request):
    try:
        return render(request, 'cart/dashboard.html', {})
    except:
        pass


# def search(request):
#     return render(request, 'cart/search.html', {})

################ functions ############
def add_pro(request):
    temp = category.objects.raw('SELECT * FROM  cart_category')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    dt=[]
    for i in value:
        dt.append(i["fields"]["name"])
    context = {"dt": dt}
    return render(request, 'cart/addproduct.html', context)


def profile_val(request):
    try:
        us = request.POST['username']
        pt = request.POST['password']
        user = authenticate(username=us, password=pt)
        uobj = User.objects.get(username=us)
        if user is not None and (uobj.customer.blacklist <= 10):
            login(request, user)
            return HttpResponseRedirect(reverse('cart:go-to-dashboard'))
        return render(request, 'cart/landing.html', {'error': 'User Blacklisted or Login Details Incorrect', })

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
        fs = FileSystemStorage(location='media/profile')
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


def profile_data(request):
    temp = User.objects.raw('SELECT * FROM  auth_user')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    print(value[0]["fields"])

    # c_user = request.user.username
    # print(c_user)
    return HttpResponse("profile updated")


def add_product(request):
    if request.user.is_authenticated and request.FILES['pro_pic']:
        uobj=User.objects.get(username=request.user.username)
        cobj = customer.objects.get(pk=uobj.customer.id)
        pro=cobj.product_set.create(title=request.POST.get("title"), quantity = request.POST.get("quantity"),
                                    description = request.POST.get("description"), price = request.POST.get("price"))

        pro_pic = request.FILES['pro_pic']
        fs = FileSystemStorage(location='media/product')
        filename = fs.save(pro_pic.name, pro_pic)
        uploaded_file_url = fs.url(filename)
        pro.pro_pic = filename
        print(filename)
        print(uploaded_file_url)

        catobj=category.objects.get(name=request.POST.get("category"))
        print(catobj.id,pro.p_id)
        pro.cat_id=catobj
        pro.save()
        # pro1.cat_id=catobj.id
        return HttpResponse("added product")


def search_product(request):
    product_name=request.POST.get("name")
    category_name=request.POST.get("category")
    price_low=request.POST.get("price_low")
    price_high = request.POST.get("price_high")
    rating=request.POST.get("rating")
    temp= Product.objects.raw('SELECT * FROM cart_product')
    data = serializers.serialize('json', temp)
    value=json.loads(data)

    dt=[]
    for i in value:
        if(i["fields"]["title"]==product_name):
            cid=i["fields"]["c_id"]
            cobj=customer.objects.get(pk=cid)
            uid=cobj.user_id
            uobj=User.objects.get(pk=uid)
            pobj=Product.objects.get(pk=i["pk"])
            dt.append((i["fields"]["title"], uobj.username,i["fields"]["price"],i["pk"],pobj.pro_pic))#productname,customername,productprice

    context={"dt":dt,"query":product_name}
    return render(request, 'cart/search.html', context)


def buy_product(request):

    quantity=request.POST.get("quantity")
    pk=34
    quantity=16
    pobj=Product.objects.get(pk=pk)
    if(pobj.quantity>=quantity):
        uname=request.user.username
        uobj=User.objects.get(username=uname)
        cobj = customer.objects.get(pk=uobj.customer.id)
        t_amt=quantity*pobj.price
        orderobj = Order()

        uobj1=User.objects.get(username=pobj.c_id)
        sobj = customer.objects.get(pk=uobj1.customer.id)

        orderobj.customer_id = cobj
        orderobj.seller_id = sobj
        orderobj.product_id=pobj
        orderobj.total_amount=t_amt
        orderobj.unitprice=pobj.price
        orderobj.quantity=quantity
        orderobj.save()

        pobj.quantity=pobj.quantity-quantity
        pobj.save()
        return HttpResponse("buy successful")
    else:
        return HttpResponse("quantity exceeded")


def seller_info(request):
    temp = Order.objects.raw('SELECT * FROM cart_order')
    data = serializers.serialize('json', temp)
    value = json.loads(data)

    dit={}
    tp=[]
    for i in value:
        if(i["fields"]["seller_id"]):
            sel_id=i["fields"]["seller_id"]
            product_id = i["fields"]["product_id"]
            sobj=customer.objects.get(pk=sel_id)
            u_id=sobj.user_id
            uobj=User.objects.get(pk=u_id)
            pobj = Product.objects.get(pk=product_id)
            dt={"seller_name":uobj.username,"product_name":pobj.title}
            tp.append(dt)

    dit = {"result": tp}

    return JsonResponse(dit)


def product_detail(request):
    quantity = request.POST.get("quantity")
    pk = request.POST.get("pk")
    pk = 34
    quantity = 16
    pobj = Product.objects.get(pk=pk)
    uobj=User.objects.get(username=pobj.c_id)
    dt=[]
    dt.extend((pobj.title,pobj.quantity,pobj.price,pobj.description,uobj.username))

    context = {"dt": dt}
    return render(request, 'cart/product.html', context)


def report_seller(request):
    username=request.POST.get("username")
    uobj=User.objects.get(username=username)
    uobj.customer.report_count+=1
    uobj.save()
    if(uobj.customer.report_count>=10):
        uobj.customer.blacklist=True
    return render(request, 'cart/dashboard.html', {})


@csrf_exempt
def seller_review(request):
    us = request.POST.get("username")
    review = request.POST.get("review")
    stars = request.POST.get("rating")

    uobj=User.objects.get(username=us)
    cobj=customer.objects.get(pk=uobj.customer.id)

    rev=c_review()
    rev.c_id=cobj
    rev.text=review
    rev.rating=stars
    rev.save()

    return HttpResponse("review added")


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

        custb = json.loads(request.body)
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
        uobj = User.objects.get(username=prod['username'])
        cobj = customer.objects.get(pk=uobj.customer.id)
        pro = cobj.product_set.create(title=prod['title'], quantity=prod['quantity'],
                                      description=prod['description'], price=prod["price"])

        catobj = category.objects.get(name=prod['category'])
        print(catobj.id, pro.p_id)
        pro.cat_id = catobj
        pro.save()

        return JsonResponse({"status": "post"})
    else:
        print('get req')
        return JsonResponse({"status": "get"})




@csrf_exempt
def get_products(request):
    temp = Product.objects.raw('SELECT * FROM cart_product')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    tp=[]
    dit={}
    for i in value:

        cid=i["fields"]["c_id"]
        cobj=customer.objects.get(pk=cid)
        uid=cobj.user_id
        uobj=User.objects.get(pk=uid)
        probj=Product.objects.get(pk=i["pk"])
        catid=probj.cat_id
        dt = {"quantity":i["fields"]["quantity"],"username":uobj.username,"title":i["fields"]["title"],"description":i["fields"]["description"],"category":str(catid)}
        tp.append(dt)
        # main.append((i["fields"]["quantity"],i["fields"]["title"], uobj.username,i["fields"]["price"]))#productname,customername,productprice
    dit={"result":tp}

    return JsonResponse(dit)




@csrf_exempt
def send(request):
    if request.method == 'GET':
        obj = customer.objects.all()
        # if (class_name == 'C_Review'):
        #     obj = c_review.objects.all()
        # if (class_name == 'Product'):
        #     obj = Product.objects.all()
        # if (class_name == 'P_Review'):
        #     obj = p_review.objects.all()
        # if (class_name == 'Category'):
        #     obj = category.objects.all()

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
