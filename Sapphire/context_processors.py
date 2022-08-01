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

def Sapphire_Product2(request):
    Product2 = Product_Type_2.objects.all()
    for prod2 in Product2:
        prod2_img = prod2.Product_Top_Background_Image
    return {'prod2_img' : prod2_img }

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

    i =0 
    for prod1 in Product1:
        if prod1.Product_Top_Background_Image:
            if i ==0 :
                prod1_img1 = prod1.Product_Top_Background_Image
                i+=1  
            else:
                prod1_img2 = prod1.Product_Top_Background_Image
              


    return {'prod1_img1' : prod1_img1,'prod1_img2' : prod1_img2 }


def Sapphire_EndSectionOfProduct(request):
    End_Section = End_Section_Of_Products.objects.all()
    for End in End_Section:
        End_sec_img = End.Background_Image
    return {'End_sec_img' : End_sec_img}