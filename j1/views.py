from django.http import HttpResponse
from django.shortcuts import render
from .models import Hereglegch

def index(request):
    return HttpResponse("welcome")

def sdfds(request):
    return render(request,'index.html')

def mmm(request):
    data=Hereglegch.objects.all()
    print(data)
    return render(request,'maa.html',{'data':data})