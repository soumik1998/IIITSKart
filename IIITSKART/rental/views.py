from django.shortcuts import render

# Create your views here.
from cart.models import customer, c_review, p_review, Product, category,Order,profile_history,user_wishlist,search_history

from django.core.files.storage import FileSystemStorage, default_storage

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

from .models import items,rent_details,item_type



def rent_dashboard(request):
    pobj=items.objects.all()
    tp=[]
    for i in pobj:
        tp.append((i.title,i.description,i.rental_price,i.quantity,i.rate,i.sold_by,i.pro_pic,i.id))
    tp.reverse()
    return HttpResponse(tp[:10])

def product_detail(request):
    pid=request.POST.get("pk")
    tp=[]
    i=items.objects.get(id=pid)
    tp.append((i.title, i.description, i.rental_price, i.quantity, i.rate, i.sold_by,i.days,i.pro_pic,i.id))
    return HttpResponse(tp)

def add_product_for_rent(request):
    uname=request.user.username
    uobj=User.objects.get(username=uname)
    cobj=customer.objects.get(id=uobj.customer.id)
    it_obj=items()
    it_obj.title=request.POST.get("title")
    it_obj.description = request.POST.get("description")
    it_obj.rental_price=request.POST.get("price")
    it_obj.quantity=request.POST.get("quantity")
    it_obj.rate=request.POST.get("rate")
    it_obj.days=request.POST.get("days")
    it_obj.sold_by=cobj

    cat_obj=item_type.objects.get(type=request.POST.get("category"))

    pro_pic = request.FILES['pro_pic']
    fs = FileSystemStorage(location='media/product')
    filename = fs.save(pro_pic.name, pro_pic)
    uploaded_file_url = fs.url(filename)
    it_obj.pro_pic = filename

    it_obj.type_id=cat_obj
    it_obj.save()


def rent_a_product(request):
    p_id=request.POST.get("pk")
    time=request.POST.get("days")
    uname=request.user.username
    uobj=User.objects.get(username=uname)
    buy_obj=customer.objects.get(id=uobj.customer.id)

    pobj=items.objects.get(id=p_id)

    uobj1 = User.objects.get(username=pobj.sold_by)
    sobj = customer.objects.get(pk=uobj1.customer.id)

    r_obj=rent_details()
    r_obj.c_id=sobj
    r_obj.rented_by=buy_obj
    r_obj.item_pro=pobj
    r_obj.amount=request.POST.get("quantity")*request.POST.get("price")*time
    r_obj.quantity=request.POST.get("quantity")
    r_obj.unit_price=request.POST.get("price")
    r_obj.save()

def search_pro(request):
    query=request.POST.get("query")
    category=request.POST.get("category")
    pri_l=request.POST.get("price_low")
    pri_h = request.POST.get("price_high")
    prname=[]
    pobj=items.objects.all()
    for i in pobj:
        if(query in i.title and category==str(i.type_id) and i.rental_price>=pri_l and i.rental_price<=pri_h):
            prname.append(i.id)
    tp=[]
    for j in prname:
        pobj_temp=items.objects.get(id=i)
        tp.append((pobj_temp.title, pobj_temp.description, pobj_temp.rental_price,
                   pobj_temp.quantity, pobj_temp.rate, pobj_temp.sold_by, pobj_temp.days,pobj_temp.pro_pic,pobj_temp.id))

    return HttpResponse(tp)


def remove(request):
    p_id = request.POST.get("pk")
    pobj=items.objects.get(id=p_id)
    pobj.delete()
    return HttpResponse("deleted")





