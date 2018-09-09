from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    
    return render(request, 'cart/index.html')

def login(request):
    name=user.username

    
    return render(request, 'cart/login.html')
