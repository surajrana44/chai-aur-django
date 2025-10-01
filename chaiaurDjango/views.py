from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("hello, world you are at home page")
   return render(request,'website/index.html')

def about(request):
    return HttpResponse("hello, world you are about page")

def contactpage(request):
    return HttpResponse("hello, world you are at contact page")


 