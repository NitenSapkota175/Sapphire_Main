from django.conf import settings
from . models import Settings
from . models import Home , Product_Type_2,About

def Sapphire_Settings(request):
    settings = Settings.objects.all()
    return {'settings' : settings}


def Sapphire_Home_image(request):
    home = Home.objects.all()
    return {'home' : home}

def Sapphire_Product2(request):
    Product2 = Product_Type_2.objects.all()
    return {'Product2' : Product2 }

def Sapphire_About_us(request):
    About_us  = About.objects.all()
    for Aboutus in About_us:
        About_image =  Aboutus.About_Us_Top_Background_Image

    return {'About_image' : About_image}