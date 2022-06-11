from ast import Return
from cgitb import Hook
from django.shortcuts import render
from django.http  import HttpResponse
from . models import Home,About
# Create your views here.
def HomePage(request):
    Home_obj = Home.objects.all()
    return render(request,'Sapphire/Home.html',{'Home_obj' : Home_obj})

def AboutUsPage(request):
    About_obj = About.objects.all()


    return render(request,'Sapphire/AboutUs.html',{'About_obj' : About_obj})