from django.shortcuts import render
from django.http import HttpResponse

def index(request): # its a HTTP request in the params that the browser would send to server
    return HttpResponse("Hello World!")

def new(request):
    return HttpResponse("New Products")