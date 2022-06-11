from ctypes import Structure
from email.mime import image
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


class SingleInstanceMixin(object):
    

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)
        super(SingleInstanceMixin, self).clean()

class Settings(SingleInstanceMixin,models.Model):
    Company_Name = models.CharField(max_length=225,default="Sapphire Commotrade Pvt.Ltd")
    Main_Logo = models.ImageField()
    
    Office_Address_Title = models.CharField(max_length=225 , default="Office Address")
    Office_Address1 = models.CharField(max_length=225,default="2nd Floor,New Golden Plaza,")
    Office_Address2 = models.CharField(max_length=225,default="Burdwan Road,")
    City_1 = models.CharField(max_length=64, default="Siliguri")
    Office_Address_Zip_Code = models.CharField(max_length=6, default="734001")



    Contact_Number_1 = PhoneNumberField()
    Contact_Number_2 = PhoneNumberField()
    Contact_Number_3 = PhoneNumberField()

    Offical_Email_Id = models.EmailField()
    Offical_Information_Email_Id = models.EmailField()

    Facebook_Page_Link = models.URLField(max_length=225,null=True,blank=True)
    Instagram_Page_Link = models.URLField(max_length=225,null=True,blank=True)
    

    Factory_Address_Title = models.CharField(max_length=255,default="Factory Address")
    Factory_Address1 = models.CharField(max_length=255,default="Demdema,Sanasekhata")
    Factory_Address2 = models.CharField(max_length=255,default="Bhutkihat,Rajgung,")
    City_2 = models.CharField(max_length=64, default="Jalpaiguri")
    Factory_Adress_Zip_Code = models.CharField(max_length=6, default="735135")


    Copyright_Field = models.CharField(max_length=225,default="2015 Sapphire Commotrade")

    Footor_Logo = models.ImageField()

    
    def __str__(self):
            return 'Settings'
    
    class Meta:
        verbose_name_plural = "Settings"


class Home(SingleInstanceMixin,models.Model):
    
    Home_Top_Background_Image = models.ImageField()
    Welcome_Title = models.CharField(max_length=225)
    Welcome_Description = models.TextField()

    What_We_Offer_Title =  models.CharField(max_length=225)
    What_We_Offer_Description = models.TextField() 

    def __str__(self):
            return 'Home'    


    class Meta:
        verbose_name_plural = "Home"  

        
              

class About(SingleInstanceMixin,models.Model):
    About_Us_Top_Background_Image = models.ImageField()
    About_Us_Title =  models.CharField(max_length=225)
    About_Us_Description = models.TextField(default='')

    OurStory_Title =  models.CharField(max_length=225)

    Where_It_All_Began_Title =  models.CharField(max_length=225)
    Where_It_All_Began_Description = models.TextField(default='')
    Where_It_All_Began_Image = models.ImageField()

    Our_Mission_Title =  models.CharField(max_length=225)
    Our_Mission_Description = models.TextField()

    Testimonial_Title =  models.CharField(max_length=225)

    What_People_Are_Saying_Title =  models.CharField(max_length=225)


    def __str__(self):
            return 'About Us'
    class Meta:
        verbose_name_plural = "About"

      

class Testimonial(models.Model):

    Title =  models.CharField(max_length=225)
    Body = models.TextField()
    Full_Name = models.CharField(max_length=225)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
     ordering = ['-updated', '-created']


class Our_Works(models.Model):
        
        Image = models.ImageField()
        
        class Meta:
            verbose_name_plural = "Our_Works"

    

class Product_Type_1(models.Model):
    Product_Name = models.CharField(max_length=225)  
    Product_Short_Description_1 = models.CharField(max_length=225)
    Product_Top_Background_Image = models.ImageField()
    Product_Short_Description_2 = models.CharField(max_length=225)
    Product_Middle_Image = models.ImageField()
    Visit_Our_Website_Title = models.CharField(max_length=225,default="Visit our website",null=True,blank=True)
    Website_Link = models.URLField(max_length=225,null=True,blank=True)
    To_Know_More_Visit_Our_Website = models.CharField(max_length=225,default="To know more visit our website",null=True,blank=True)
    Introduction_Section_Title = models.CharField(max_length=255) 
    Introduction_Section_Description = models.TextField()
    
    Introduction_Section_Image1 = models.ImageField()
    Introduction_Section_Image2 = models.ImageField()
    Why_Us_Title = models.CharField(max_length=225) 
    Why_Us_Description = models.TextField()
    Why_Us_Image1 = models.ImageField()
    Why_Us_Image2 = models.ImageField()
    Why_Us_Image3 = models.ImageField()
    
    Product_Structure_Image = models.ImageField()

  
    def __str__(self):
            return self.Product_Name
    class Meta:
         verbose_name_plural = "Product_Type_1"    


class Product_Type1_Structure(models.Model):
    
    Product_name = models.ForeignKey(Product_Type_1 , on_delete=models.CASCADE)
    Product1_Structure_Title = models.CharField(max_length=225,null=True,blank=True)
    Product1_Structure_Short_Description = models.TextField(null=True,blank=True)
   
 

class Product_Type1_Features(models.Model):
        Product_name = models.ForeignKey(Product_Type_1 , on_delete=models.CASCADE)
        ProductType1_Feature = models.CharField(max_length=225,null=True,blank=True)
     
class Product_Type1_Assurances(models.Model):
        Product_name = models.ForeignKey(Product_Type_1 , on_delete=models.CASCADE)
        ProductType1_Assurance = models.CharField(max_length=225,null=True,blank=True)
        
        
####### Product type 2 models starts form here ########
class Product_Type_2(models.Model):
   

    Product_Name = models.CharField(max_length=225)
    Product_Short_Description_1 = models.CharField(max_length=225)
    Product_Top_Background_Image = models.ImageField()
    Product_Short_Description_2 = models.CharField(max_length=225)
    Product_Middle_Image = models.ImageField()
    Visit_Our_Website_Title = models.CharField(max_length=225,default="Visit our website",null=True,blank=True)
    Website_Link = models.URLField(max_length=225,null=True,blank=True)
    To_Know_More_Visit_Our_Website = models.CharField(max_length=225,default="To know more visit our website",null=True,blank=True)
    
    Introduction_Section_Title = models.CharField(max_length=255) 
    Introduction_Section_Description = models.TextField()
    Introduction_Section_Image = models.ImageField()
    
    Why_Us_Title = models.CharField(max_length=225) 
    Why_Us_Description = models.TextField()
    Why_Us_Image1 = models.ImageField()
    Why_Us_Image2 = models.ImageField()


    def __str__(self):
            return self.Product_Name
    class Meta:
         verbose_name_plural = "Product_Type_2"




class Product_Type2_Features(models.Model):
        Product_name = models.ForeignKey(Product_Type_2 , on_delete=models.CASCADE)
        ProductType2_Feature = models.CharField(max_length=225,null=True,blank=True)
      
class Product_Type2_Assurance(models.Model):
    Product_name = models.ForeignKey(Product_Type_2,on_delete=models.CASCADE)
    ProductType2_Assurance = models.CharField(max_length=225,null=True,blank=True)

class End_Section_Of_Products(SingleInstanceMixin,models.Model):
    Background_Image = models.ImageField()

    logo1 = models.ImageField()
    Title1 = models.CharField(max_length=225)
    Description1 = models.CharField(max_length=225,null=True,blank=True)

    logo2 = models.ImageField()
    Title2 = models.CharField(max_length=225)
    Description2 = models.CharField(max_length=225,null=True,blank=True)

    logo3 = models.ImageField()
    Title3 = models.CharField(max_length=225)
    Description3 = models.CharField(max_length=225,null=True,blank=True)

    def __str__(self):
            return 'End_Section_Of_Products'

    class Meta:
         verbose_name_plural = "End_Section_Of_Products"

class Contact(SingleInstanceMixin,models.Model):
    Background_Image = models.ImageField()
    Title = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
            return 'Contact Us'
    
    class Meta:
         verbose_name_plural = "Contact Us"



