from django.shortcuts import render

# Create your views here.
from cart.models import customer, c_review, p_review, Product, category,Order,profile_history,user_wishlist,search_history
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
import requests
from django.shortcuts import render
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .serializers import CustomerSerializer, C_reviewSerializer, P_reviewSerializer, ProductSerializer, CategorySerializer
import base64
import os, random, string
import os.path
from .models import items,rent_details,item_type

def add_for_rent(request):
    uname=request.user.username
    uobj=User.objects.get(username=uname)
    cobj=customer.objects.get(id=uobj.customer.id)
    it_obj=items()
    it_obj.title=request.POST.get("title")
    it_obj.description = request.POST.get("description")
    it_obj.rental_price=request.POST.get("price")
    it_obj.quantity=request.POST.get("quantity")
    it_obj.sold_by=cobj

    cat_obj=item_type.objects.get(type=request.POST.get("category"))

    it_obj.type_id=cat_obj
    it_obj.save()


def rent_a_product(request):
    p_id=request.POST.get("pk")
    uname=request.user.username
    uobj=User.objects.get(username=uname)
    cobj=customer.objects.get(id=uobj.customer.id)

