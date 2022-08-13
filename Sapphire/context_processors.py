from . models import End_Section_Of_Products, Settings
from . models import Home , Product_Type_2,About,Contact,Product_Type_1,End_Section_Of_Products

def Sapphire_Settings(request):
    settings = Settings.objects.all()
    return {'settings' : settings}


def Sapphire_Home_image(request):
    home = Home.objects.all()
    for h in home:
        home_img = h.Home_Top_Background_Image 
    return {'home_img' : home_img}

def Sapphire_About_us(request):
    About_us  = About.objects.all()
    for Aboutus in About_us:
        About_image =  Aboutus.About_Us_Top_Background_Image

    return {'About_image' : About_image}

def Sapphire_contactus(request):
    contactus = Contact.objects.all()
    for cont in contactus:
        contactus_img = cont.Background_Image
    return {'contactus_img' : contactus_img}


def Sapphire_Product1(request):
    Product1 = Product_Type_1.objects.all()
    

    return {'Product1' : Product1 }

def Sapphire_Product2(request):
    Product2 = Product_Type_2.objects.all()

    return {'Product2' : Product2 }


def Sapphire_EndSectionOfProduct(request):
    End_Section = End_Section_Of_Products.objects.all()
    for End in End_Section:
        End_sec_img = End.Background_Image
    return {'End_sec_img' : End_sec_img}