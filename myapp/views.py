from django.shortcuts import render,HttpResponse,redirect
from myapp.models import *




def home(request):
    return render(request,'index.html')

def homea(request):
    return redirect(home)

def project(request):
    return render(request,'about.html')

def clock(request):
    return render(request,'clock.html')

def firework(request):
    return render(request,'fire1.html')

def qrcodemaker(request):
    return render(request,'qrcodemaker.html')




