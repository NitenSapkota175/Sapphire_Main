from ast import Return
from cgitb import Hook
from email import message
from multiprocessing import context
from django.conf import settings
from django.shortcuts import redirect, render
from django.http  import HttpResponse
from . models import End_Section_Of_Products, Home,About, Product_Type_1, Testimonial,Product_Type_2,Our_Works,Contact,Settings
from django.core.mail import send_mail,BadHeaderError
from Sapphire import models
# Create your views here.
def HomePage(request):
    Home_obj = Home.objects.all()
    Product1 = Product_Type_1.objects.all()[0:2]
    Product2 = Product_Type_2.objects.all()[0:1]
    

    context = { 'Home_obj' : Home_obj ,   'Product1' : Product1 , 'Product2' : Product2  }
    return render(request,'Sapphire/Home.html',context)

def AboutUsPage(request):
    About_obj = About.objects.all()
    Testimonial_obj = Testimonial.objects.all()

    context = { 'Testimonial_obj' :   Testimonial_obj  ,   'About_obj'  :  About_obj }

    return render(request,'Sapphire/AboutUs.html',context)


def ProductPage(request):

    Product1 = Product_Type_1.objects.all()
    Product2 =Product_Type_2.objects.all()
    End_Section = End_Section_Of_Products.objects.all()

    context = {'Product1' : Product1 ,'Product2' : Product2 , 'End_Section' : End_Section}
    return render(request,'Sapphire/Products.html',context)


def ProductType1(request,pk):

    Product1 = Product_Type_1.objects.filter(id=pk)
    End_Section = End_Section_Of_Products.objects.all()
    context = {'Product1' : Product1 , 'End_Section' : End_Section }
   
    
    return render(request,'Sapphire/ProductType1.html',context)

def ProductType2(request,pk):
    Product2 = Product_Type_2.objects.filter(id=pk)
    End_Section = End_Section_Of_Products.objects.all()
    context = {'Product2' : Product2 , 'End_Section' : End_Section }
    return render(request,'Sapphire/ProductType2.html',context)


def OurWork(request):

    Our_works = Our_Works.objects.all()
    context = {'Our_works' : Our_works }
    return render(request,'Sapphire/OurWork.html',context)

def EndSectionOfProduct(request):
    End_Section = End_Section_Of_Products.objects.all()
    context = {'End_Section' : End_Section }
    return render(request,'Sapphire/EndsectionofEveryProduct.html',context)

def Contactus(request):



    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        number = request.POST.get('phoneno')
        message_body = request.POST.get('help')
        
        if name and email and message_body and number:
            try:
                send_mail(name,message_body,email, ['pointers200@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('Home')
        else:
    
            return HttpResponse('Make sure all fields are entered and valid.')
    
    
    
        
    contactus = Contact.objects.all()
    settings = Settings.objects.all()
    context = {'contactus' : contactus , 'settings' : settings }


    return render(request,'Sapphire/Contactus.html',context)

