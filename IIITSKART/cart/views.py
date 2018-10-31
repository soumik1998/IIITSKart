from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import transaction
from django.core.files.storage import FileSystemStorage, default_storage
from django.http import *
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import customer, c_review, p_review, Product, category,Order,profile_history,user_wishlist,search_history
from .serializers import CustomerSerializer, C_reviewSerializer, P_reviewSerializer, ProductSerializer, CategorySerializer


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
    if User.is_authenticated == True and User.is_anonymous == False and User.is_active == True:
        return render(request, 'cart/dashboard.html')
    else:
        dt = []
        dt.append((User.objects.all().count(), Product.objects.all().count(), Order.objects.all().count()))
        print(dt)
        return render(request, 'cart/landing.html', {"dt": dt})


def sign_up(request):
    dt = []
    dt.append((User.objects.all().count(), Product.objects.all().count(), Order.objects.all().count()))
    print(dt)
    return render(request, 'cart/landing.html', {"dt": dt})


def dashboard(request):

    return render(request, 'cart/dashboard.html')


def login_page(request):
    dt=[]
    dt.append((User.objects.all().count(),Product.objects.all().count(),Order.objects.all().count()))
    print(dt)
    return render(request, 'cart/landing.html', {"dt":dt})



def logout_view(request):
    logout(request)
    dt = []
    dt.append((User.objects.all().count(), Product.objects.all().count(), Order.objects.all().count()))
    print(dt)
    return render(request, 'cart/landing.html', {"dt": dt})


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
            cobj = customer.objects.get(pk=cid)
            uid = cobj.user_id
            uobj = User.objects.get(pk=uid)
            pobj = Product.objects.get(pk=i["pk"])
            revobj = c_review.objects.filter(s_id=cobj)
            avgrating=[]
            for j in revobj:
                avgrating.append(j.rating)
            if(len(avgrating)):
                rating="%.1f" %(sum(avgrating)/len(avgrating))
            else:
                rating=0

            if(uobj.username not in request.user.username):
                dt1.append((i["fields"]["title"][:18], uobj.username, i["fields"]["price"], pobj.pro_pic,int(i["pk"]),rating))
                print(dt1)
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
            uobj.is_active = True
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


def registration_email_link(request):
    if request.method == 'POST':

        if User.objects.filter(username=request.POST.get('email', "")).count() == 0:
            uobj = User()
            uobj.is_active = False
            uobj.username = request.POST.get('username', "")
            uobj.first_name = request.POST.get('first_name', "")
            uobj.last_name = request.POST.get('last_name', "")
            uobj.email = request.POST.get('email', "")
            uobj.set_password(request.POST.get('password', ""))

            current_site = get_current_site(request)
            print(uobj)
            mail_subject = 'Activate your IIITSCart account.'
            message = render_to_string('acc_active_email.html', {
                'user': uobj.username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(uobj.username)).decode(),
                'token': account_activation_token.make_token(uobj),
            })
            to_email = request.POST.get('email', "")
            # print(to_email)
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            uobj.save()

            uobj_tmp = User.objects.get(username=request.POST.get('username', ""))
            uobj_tmp.customer.blacklist = False
            uobj_tmp.save()

            # cobj=customer.objects.get(pk=uobj_tmp.customer.id)


            # user = authenticate(username=uobj.username, password=request.POST.get('password', ""))
            # if user is not None:
            #     login(request, user)
            #     return HttpResponseRedirect(reverse('cart:go-to-dashboard'))
            return render(request, 'cart/landing.html', {})

        else:

            return render(request, 'cart/landing.html', {})


def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:

        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(username=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


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
    search_history(product_name, request)
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
    # return HttpResponse(value)
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
            dt.append((i["fields"]["title"][:18], uobj.username, i["fields"]["price"],pobj.pro_pic, i["pk"],rating))#productname,customername,productprice

    temp = Product.objects.raw('SELECT * FROM  cart_product')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    num = []
    for i in value:
        num.append(i["fields"]["title"])
    context={"dt":dt,"query":product_name,"num":len(num)}

    return render(request, 'cart/search.html', context)

def srch_history(product_name,request):
    uname=request.user.username
    uobj=User.objects.get(username=uname)
    cobj=customer.objects.get(pkk=uobj.customer.id)

    srcobj=search_history()
    srcobj.c_id=cobj
    srcobj.searchtext=product_name
    srcobj.save()

def buy_product(request):

    quantity=int(request.POST.get("quantity"))
    pk=request.POST.get("pk")

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
        avg_rating=abs(sum(rat_temp)/len(rat_temp))
        rating="%.1f" %(abs(sum(rat_temp)/len(rat_temp)))
    else:
        avg_rating=0.0
        rating=0


    dt=[]
    rate=[]
    d_rate=[]
    for i in range(int(avg_rating)):
        rate.append(i)
    for i in range(5-int(avg_rating)):
        d_rate.append(i)

    dt.extend((pobj.title,pobj.quantity,pobj.price,pobj.description,uobj.username,pobj.pro_pic,rate,d_rate,int(pk),rating))
    print(rev_text)
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


def add_to_wishlist(request):
    pid=request.POST.get("pk")
    uname=request.user.username
    uobj=User.objects.get(username=uname)
    cobj=customer.objects.get(pk=uobj.customer.id)
    pobj=Product.objects.get(pk=pid)

    wl=user_wishlist()
    wl.c_id=cobj
    wl.wish=pobj
    wl.save()

    return render(request, 'cart/success.html', {'msg': " Added to the wishlist"})

def view_wishlist(request):
    uname=request.user.username
    uobj=User.objects.get(username=uname)


    dt1=[]

    temp = user_wishlist.objects.raw('SELECT * FROM  cart_user_wishlist')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    for i in value:
        if(uobj.customer.id==i["fields"]["c_id"]):
            print("in")
            pobj = Product.objects.get(pk=i["fields"]["wish"])
            sid = pobj.c_id_id
            sobj = customer.objects.get(pk=sid)
            uid=sobj.user_id
            uobj1=User.objects.get(pk=uid)
            revobj=c_review.objects.all().filter(s_id=sobj)
            #print("rttr",revobj)
            temp=[]
            for j in revobj:
                print(j.rating)
                temp.append(j.rating)
            if(len(temp)==0):
                rating=0
            else:
                rating=sum(temp)/len(temp)
            dt1.append((pobj.title, uobj1.username, pobj.price, i["fields"]["wish"], pobj.pro_pic,rating))
            print(dt1)
        return render(request, 'cart/order.html', {"dt1":dt1})


def edit_wishlist(request):
    proid=request.POST.get("pk")
    pobj=Product.objects.get(pk=proid)
    uname = request.user.username
    uobj = User.objects.get(username=uname)
    cobj=customer.objects.get(pk=uobj.customer.id)
    wl=user_wishlist.objects.filter(wish=pobj,c_id=cobj)
    wl.delete()
    return HttpResponse("deleted")


def add_a_comment(request):
    proid = request.POST.get("pk")
    proid=8
    pobj = Product.objects.get(pk=proid)

    uname = request.user.username
    uobj = User.objects.get(username=uname)
    cobj = customer.objects.get(pk=uobj.customer.id)

    sid=pobj.c_id_id
    sobj = customer.objects.get(pk=sid)
    if(Order.objects.filter(customer_id=cobj,seller_id=sobj,product_id=pobj)):
        revobj=c_review()
        revobj.b_id=cobj
        revobj.s_id=sobj
        revobj.rating=5#request.POST.get('rating')
        revobj.text="rerliable"#request.POST.get("commment")
        revobj.save()
        return HttpResponse("comment added")
    else:
        return HttpResponse("person who bought can comment")









#######################################################################
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
    sel_usr=request.GET.get("seller_username")
    print(sel_usr)
    uobj=User.objects.get(username=sel_usr)
    temp = c_review.objects.raw('SELECT * FROM cart_c_review')
    data = serializers.serialize('json', temp)
    value = json.loads(data)
    tp = []
    dit = {}
    for i in value:
        if(i["fields"]["c_id"]== uobj.customer.id):
                custRevObj=c_review.objects.get(pk=int(i["pk"]))
                dt = {"text": custRevObj.text, "rating": custRevObj.rating}
                tp.append(dt)
    dit = {"username": uobj.username, "address": uobj.customer.address, "phone": uobj.customer.phone, "result": tp}
    print(dit)
    return JsonResponse(dit)

@csrf_exempt
def seller_review_api(request):
    rev = json.loads(request.body)
    print("sgdshdg")
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