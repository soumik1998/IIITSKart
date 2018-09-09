from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
from django.http import HttpResponse
from social_django.models import *


def index(request):
    print(request.user.username, request.user.email)
    print(request.user.social_auth.get(uid=request.user.email))
    return JsonResponse({
        'user': model_to_dict(request.user)
    }, safe=False)

def signup(request):
    
    return render(request, 'cart/signup.html')


