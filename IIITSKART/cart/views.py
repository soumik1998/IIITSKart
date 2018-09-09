from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
from django.http import HttpResponse
from social_django.models import *


def index(request):

    return JsonResponse({
        'user': model_to_dict(request.user)
    }, safe=False)

def login(request):
    
    return render(request, 'cart/login.html')


def home(request):
    return render(request, "cart/landing.html", {})



