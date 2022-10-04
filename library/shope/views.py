from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"store/index.html")

def about(request):
    return render(request,"store/about.html")
