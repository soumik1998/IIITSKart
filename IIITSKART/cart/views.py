from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.http import *
from django.contrib.auth import logout
import requests


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

