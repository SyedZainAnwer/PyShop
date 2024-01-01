from django.shortcuts import render
from django.http import HttpResponse
from.models import Product

def index(request): # its a HTTP request in the params that the browser would send to server
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products}) # key-value pair in 3rd param

def new(request):
    return HttpResponse("New Products")