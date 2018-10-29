from django.contrib.auth.decorators import login_required
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
from .models import customer, c_review, p_review, Product, category,Order,profile_history
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
    if User.is_authenticated:
        return render(request, 'cart/dashboard.html')
    else:
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


@login_required
def go_to_dashboard(request):
        temp = Product.objects.raw('SELECT * FROM  cart_product')
        data = serializers.serialize('json', temp)
        value = json.loads(data)
        dt=[]
        dt1=[]
        for i in value:
            dt.append(i["fields"]["title"])

            cid = i["fields"]["c_id"]
            print(cid)
            cobj = customer.objects.get(pk=cid)
            uid = cobj.user_id
            uobj = User.objects.get(pk=uid)
            pobj = Product.objects.get(pk=i["pk"])
            try:
                revobj = c_review.objects.get(s_id=cid)
                rating=revobj.rating
            except:
                rating=0


            if(uobj.username not in request.user.username):
                dt1.append((i["fields"]["title"], uobj.username, i["fields"]["price"], i["pk"], pobj.pro_pic,i["pk"],rating))
                # productname,customername,productprice
        dt1.reverse()
        context = {"num": len(dt),"dt1":dt1[:10]}


        return render(request, 'cart/dashboard.html', context)


@login_required
def profile_view(request):
    temp = Product.objects.raw('SELECT * FROM  cart_product')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    num = []
    for i in value:
        num.append(i["fields"]["title"])
    return render(request, 'cart/profile.html', {"num":len(num)})


def customer_act(request):
    return render(request,'cart/order.html',{})


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
            uobj.set_password(request.POST.get('password', ""))
            uobj.save()

            uobj_tmp=User.objects.get(username=request.POST.get('username', ""))
            uobj_tmp.customer.blacklist = False
            uobj_tmp.save()

            cobj=customer.objects.get(pk=uobj_tmp.customer.id)


            user = authenticate(username=uobj.username, password=request.POST.get('password', ""))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('cart:go-to-dashboard'))

        else:
            print("else")
            return render(request, 'cart/landing.html', {})


@login_required
def profile_photo_upload(request):
    if request.method == 'POST' and request.FILES['avatar']:
        print(request.FILES['avatar'])
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
        return render(request,'cart/success.html',{'msg':" Product Added Successfully"})


def search_product(request):
    product_name=request.POST.get("name")
    category_name=request.POST.get("category")
    price_low=request.POST.get("price_low")
    price_high = request.POST.get("price_high")
    rating=request.POST.get("rating")

    category_name="all"
    price_low=0
    price_high=100000000
    rating=0

    temp= Product.objects.raw('SELECT * FROM cart_product')
    data = serializers.serialize('json', temp)
    value=json.loads(data)
    dt=[]

    uobj_tmp=User.objects.get(username=request.user.username)
    cid_tmp=uobj_tmp.customer.id
    cobj_temp= customer.objects.get(pk=cid_tmp)

    for i in value:
        catobj=category.objects.get(pk=i["fields"]["cat_id"])
        if(category_name=="all"):
            cat_name="all"
        else:
            cat_name=catobj.name
        if((product_name.lower() in (str(i["fields"]["title"].lower())))
                and (i["fields"]["c_id"] != cid_tmp)
                and(int(i["fields"]["price"])>price_low)
                and (int(i["fields"]["price"])<price_high)
                and (cat_name==category_name)) :
            print("yes")
            cid=i["fields"]["c_id"]
            cobj=customer.objects.get(pk=cid)
            uid=cobj.user_id
            uobj=User.objects.get(pk=uid)
            pobj=Product.objects.get(pk=i["pk"])
            try:
                revobj=c_review.objects.get(s_id=cid)
                rating=revobj.rating
            except:
                rating=0
            dt.append((i["fields"]["title"], uobj.username, i["fields"]["price"], i["pk"],pobj.pro_pic, i["pk"],rating))#productname,customername,productprice

    temp = Product.objects.raw('SELECT * FROM  cart_product')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    num = []
    for i in value:
        num.append(i["fields"]["title"])
    context={"dt":dt,"query":product_name,"num":len(num)}

    return render(request, 'cart/search.html', context)


def buy_product(request):

    quantity=int(request.POST.get("quantity"))
    pk=int(request.POST.get("pk"))

    print(type(pk),type(quantity))
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
        return render(request, 'cart/success.html', {'msg': "Order Placed Successfully"})
    else:
        return render(request, 'cart/error.html', {'msg': "Product Quantity Exceeded"})


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
    flag=0
    pk = request.POST.get("pk")
    pobj = Product.objects.get(pk=pk)
    uobj=User.objects.get(username=pobj.c_id)
    temp = c_review.objects.raw('SELECT * FROM cart_c_review')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    rat_temp=[]
    rev_text=[]
    for i in value:
        if(i["fields"]["s_id"]==int(uobj.customer.id)):
            revpk=i["pk"]
            revobj = c_review.objects.get(pk=int(revpk))
            rat_temp.append(i["fields"]["rating"])
            bid=i["fields"]["b_id"]
            cobj = customer.objects.get(pk=bid)
            uid=cobj.user_id
            uobj1=User.objects.get(pk=uid)
            rev_text.append((uobj1.username,revobj.text))



    if(len(rat_temp)>0):
        flag=1
        avg_rating=abs(sum(rat_temp)/len(rat_temp))
    else:
        avg_rating=0.0
    if(flag==1):
        print("flag1s")
        dt=[]
        rate=[]
        d_rate=[]
        for i in range(int(avg_rating)):
            rate.append(i)
        for i in range(5-int(avg_rating)):
            d_rate.append(i)

        dt.extend((pobj.title,pobj.quantity,pobj.price,pobj.description,uobj.username,pobj.pro_pic,rate,d_rate,pk,avg_rating))
        print(rev_text)
        context = {"dt": dt,"rev_text":rev_text}
        return render(request, 'cart/product.html', context)
    else:
        dt=[]
        rate=[]
        d_rate=[]
        for i in range(int(avg_rating)):
            rate.append(i)
        for i in range(5-int(avg_rating)):
            d_rate.append(i)

        dt.extend((pobj.title,pobj.quantity,pobj.price,pobj.description,uobj.username,pobj.pro_pic,rate,d_rate,"not reviewed yet",pk,avg_rating))

        context = {"dt": dt,"rev_text":rev_text}
        return render(request, 'cart/product.html', context)



def customer_activity_sell(request):
    uname=request.user.username
    uobj=User.objects.get(username=uname)
    id=uobj.customer.id

    temp = Order.objects.raw('SELECT * FROM cart_order')
    data = serializers.serialize('json', temp)
    value = json.loads(data)

    dt=[]
    for i in value:
        if(i["fields"]["seller_id"]==id):
            pobj = Product.objects.get(pk=i["fields"]["product_id"])
            temp = i["fields"]["order_date"]
            cid = i["fields"]["customer_id"]
            cobj1 = customer.objects.get(pk=cid)
            uobj1=User.objects.get(pk=cobj1.user_id)
            ind = temp.find("T")
            date = temp[:ind]
            dt.append((pobj.title, i["fields"]["quantity"], i["fields"]["total_amount"], uobj1.username, date))


    temp = category.objects.raw('SELECT * FROM  cart_category')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    dt1=[]
    for i in value:
        dt1.append(i["fields"]["name"])

    temp = Product.objects.raw('SELECT * FROM  cart_product')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    num = []
    for i in value:
        num.append(i["fields"]["title"])

    dt.reverse()
    context = {"dt1": dt1,"dt":dt,"num":len(num)}
    return render(request, 'cart/addproduct.html', context)


def customer_activity_buy(request):
    uname=request.user.username
    uobj=User.objects.get(username=uname)
    id=uobj.customer.id

    temp = Order.objects.raw('SELECT * FROM cart_order')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    # return HttpResponse(value)
    dt=[]
    # return HttpResponse(value)
    for i in value:
        if i["fields"]["customer_id"] == id:
            if(i["fields"]["product_id"]):
                pobj = Product.objects.get(pk=i["fields"]["product_id"])
                sid=i["fields"]["seller_id"]
                cobj1=customer.objects.get(pk=sid)
                uobj1=User.objects.get(pk=cobj1.user_id)
                temp = i["fields"]["order_date"]
                ind = temp.find("T")
                date = temp[:ind]
                dt.append((pobj.title, i["fields"]["quantity"], i["fields"]["total_amount"], uobj1.username, date))
    temp = Product.objects.raw('SELECT * FROM  cart_product')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    num = []
    for i in value:
        num.append(i["fields"]["title"])

    dt.reverse()
    context = {"dt": dt,"num":len(num)}
    return render(request, 'cart/order.html', context)


@transaction.atomic
def update_profile(request):


    history_profile(request)
    username=request.user.username
    uobj=User.objects.get(username=username)
    uobj.first_name=request.POST.get("firstname")
    uobj.last_name=request.POST.get("lastname")
    uobj.customer.phone=request.POST.get("phone")
    uobj.customer.address=request.POST.get("address")
    uobj.email=request.POST.get("email")
    uobj.save()

    return render(request, 'cart/success.html', {'msg': "Update Successful"})



def history_profile(request):

    username=request.user.username
    uobj=User.objects.get(username=username)
    cobj = customer.objects.get(pk=uobj.customer.id)
    tobj=profile_history()
    tobj.c_id=cobj
    tobj.firstname=uobj.first_name
    tobj.lastname=uobj.last_name
    tobj.phone=uobj.customer.phone
    tobj.address=uobj.customer.address
    tobj.email=uobj.email
    tobj.save()


def report_seller(request):
    username=request.POST.get("username")
    uobj=User.objects.get(username=username)
    uobj.customer.report_count+=1
    uobj.save()
    if(uobj.customer.report_count>=10):
        uobj.customer.blacklist = True
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


def test_api(request):
    if request.method == 'POST':
        prod = json.loads(request.body)
        print(prod['category'])

        return JsonResponse({"status": "post"})
    else:
        print('get req')
        return JsonResponse({"status": "get"})



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


@csrf_exempt
def get_userdetails(request):
    temp = c_review.objects.raw('SELECT * FROM cart_c_review')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    tp=[]
    dit={}
    for i in value:

        cid=i["fields"]["c_id"]
        cobj=customer.objects.get(pk = cid)
        uid=cobj.user_id
        print(uid,cobj.address)
        uobj = User.objects.get(pk = uid)
        custRevObj = c_review.objects.get(pk = i["pk"])
        catid = custRevObj.c_id
        rev = custRevObj.text
        print(catid,rev)
        if (str(catid )=='chinmay'):
            print("sdfsdf")
            dt={"text":custRevObj.text,"rating":custRevObj.rating}
            tp.append(dt)
    dit={"username":str(catid),"address":cobj.address,"phone":cobj.phone,"result":tp}
    print(dit)
    return JsonResponse(dit)

@csrf_exempt
def seller_review_api(request):
    rev = json.loads(request.body)

    us = rev["username"]
    review = rev["text"]
    stars = rev["rating"]

    uobj=User.objects.get(username=us)
    cobj=customer.objects.get(pk=uobj.customer.id)

    rev=c_review()
    rev.c_id=cobj
    rev.text=review
    rev.rating=stars
    rev.save()
    print("gfhfhg")
    return HttpResponse("review added")

