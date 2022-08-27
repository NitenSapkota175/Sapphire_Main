from email import message
from django.db import models
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe
class SingleInstanceMixin(object):
    

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)
        super(SingleInstanceMixin, self).clean()

class ZeroInstanceMixin(object):
    
    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)
        super(ZeroInstanceMixin, self).clean()

class Settings(SingleInstanceMixin,models.Model):
    Company_Name = models.CharField(max_length=225,default="Sapphire Commotrade Pvt.Ltd")
    Main_Logo = models.ImageField()
    
    Office_Address_Title = models.CharField(max_length=225 , default="Office Address")
    Office_Address1 = models.CharField(max_length=225,default="2nd Floor,New Golden Plaza,")
    Office_Address2 = models.CharField(max_length=225,default="Burdwan Road,")
    City_1 = models.CharField(max_length=64, default="Siliguri")
    Office_Address_Zip_Code = models.CharField(max_length=6, default="734001")



    Contact_Title = models.CharField(max_length=225,null=True,blank=True)
    Contact_Number_1 = PhoneNumberField()
    Contact_Number_2 = PhoneNumberField()
    Contact_Number_3 = PhoneNumberField()

    Email_Title = models.CharField(max_length=225,null=True,blank=True)
    Offical_Email_Id = models.EmailField()
    Offical_Information_Email_Id = models.EmailField()

    Facebook_Page_Link = models.URLField(max_length=225,null=True,blank=True)
    Instagram_Page_Link = models.URLField(max_length=225,null=True,blank=True)
    LinkedIn_Page_Link = models.URLField(max_length=225,null=True,blank=True)
    Twitter_Page_Link = models.URLField(max_length = 225,null = True,blank= True)

    Factory_Address_Title = models.CharField(max_length=255,default="Factory Address")
    Factory_Address1 = models.CharField(max_length=255,default="Demdema,Sanasekhata")
    Factory_Address2 = models.CharField(max_length=255,default="Bhutkihat,Rajgung,")
    City_2 = models.CharField(max_length=64, default="Jalpaiguri")
    Factory_Adress_Zip_Code = models.CharField(max_length=6, default="735135")


    Copyright_Field = models.CharField(max_length=225,default="2015 Sapphire Commotrade")

    Footor_Logo = models.ImageField()

    def Main_logo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Main_Logo.url))

    def Footor_logo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Footor_Logo.url))

  
   


    
    def __str__(self):
            return 'Settings'
    
    class Meta:
        verbose_name_plural = "        Settings"


class Home(SingleInstanceMixin,models.Model):
    
    Home_Top_Background_Image = models.ImageField()
    Welcome_Title = models.CharField(max_length=225)
    Welcome_Description = models.TextField()

    What_We_Offer_Title =  models.CharField(max_length=225)
    What_We_Offer_Description = models.TextField() 

    def __str__(self):
            return 'Home'    

    def Home_Top_Background_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Home_Top_Background_Image.url))

    class Meta:
        verbose_name_plural = "       Home"  

        
              

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

    def About_Us_Top_Background_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.About_Us_Top_Background_Image.url))

    def Where_It_All_Began_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Where_It_All_Began_Image.url))




    def __str__(self):
            return 'About Us'
    class Meta:
        verbose_name_plural = "      About"

      

class Testimonial(models.Model):

 

    Title =  models.CharField(max_length=225)
    Body = models.TextField()
    Full_Name = models.CharField(max_length=225)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
     ordering = ['-updated', '-created']
     verbose_name_plural = "     Testimonials"


class Our_Works(models.Model):
        
        Image1 = models.ImageField(blank=True,null=True)
        Image2 = models.ImageField(blank=True,null=True)
        Image3 = models.ImageField(blank=True,null=True)

        def image1(self):
                return mark_safe('<img src="{}" width="100" />'.format(self.Image1.url))

        def image2(self):
                return mark_safe('<img src="{}" width="100" />'.format(self.Image2.url))

        def image3(self):
                return mark_safe('<img src="{}" width="100" />'.format(self.Image3.url))

        

        class Meta:
            verbose_name_plural = "  Our_Works"

    

class Product_Type_1(models.Model):
    Product_Name =models.CharField(max_length=225,null=True)
    Product_Short_Description_1 = models.CharField(max_length=225)
    Product_Top_Background_Image = models.ImageField()
    Product_Short_Description_2 = models.CharField(max_length=225)
    Product_HomePage_Image = models.ImageField(null=True,blank=True)
    Product_HomePage_Description = models.TextField(null=True , blank=True)
    Product_ProductPage_Image  =  models.ImageField(null=True,blank=True) 
    Product_ProductPage_Description = models.TextField(null=True,blank=True)
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
    
    def Product_ProductPage_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_ProductPage_Image.url))

    def Product_HomePage_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_HomePage_Image.url))
    
    def Product_Top_Background_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_Top_Background_Image.url))

    def Product_Middle_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_Middle_Image.url))
    
    def Introduction_Section_image1(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Introduction_Section_Image1.url))

    def Introduction_Section_image2(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Introduction_Section_Image2.url))

    def Why_Us_image1(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Why_Us_Image1.url))

    def Why_Us_image2(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Why_Us_Image2.url))

    def Why_Us_image3(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Why_Us_Image3.url))
        
    def Product_Structure_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_Structure_Image.url))
          



    def __str__(self):
            return self.Product_Name
    class Meta:
         verbose_name_plural = "    Product_Type_1"    


class Product_Type1_Structure(models.Model):
    
    Product_name = models.ForeignKey(Product_Type_1 , on_delete=models.CASCADE)
    Product1_Structure_Title = models.CharField(max_length=225,null=True,blank=True,default='')
    Product1_Structure_Short_Description = models.TextField(null=True,blank=True)
   
 

class Product_Type1_Features(models.Model):
        Product_name = models.ForeignKey(Product_Type_1 , on_delete=models.CASCADE)
        ProductType1_Feature = models.CharField(max_length=225,null=True,blank=True)
     
class Product_Type1_Assurances(models.Model):
        Product_name = models.ForeignKey(Product_Type_1 , on_delete=models.CASCADE)
        ProductType1_Assurance = models.CharField(max_length=225,null=True,blank=True)
        
        
####### Product type 2 models starts form here ########
class Product_Type_2(models.Model):
   

    Product_Name = models.CharField(max_length=225,null=True)
    Product_Short_Description_1 = models.CharField(max_length=225)
    Product_Top_Background_Image = models.ImageField()
    Product_Short_Description_2 = models.CharField(max_length=225)
    Product_HomePage_Image = models.ImageField(null=True,blank=True) 
    Product_HomePage_Description = models.TextField(null=True , blank=True)
   
    Product_ProductPage_Image  =  models.ImageField(null=True,blank=True) 
    Product_ProductPage_Description = models.TextField(null=True,blank=True)
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

    def Product_Top_Background_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_Top_Background_Image.url))

    def Product_ProductPage_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_ProductPage_Image.url))



    def Product_HomePage_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_HomePage_Image.url))




    def Product_Middle_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_Middle_Image.url))
    
    def Introduction_Section_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Introduction_Section_Image.url))

    def Why_Us_image1(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Why_Us_Image1.url))

    def Why_Us_image2(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Why_Us_Image2.url))


    def __str__(self):
            return self.Product_Name
    class Meta:
         verbose_name_plural = "   Product_Type_2"




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

    def Logo1(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.logo1.url))

    def Logo2(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.logo2.url))

    def Logo3(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.logo3.url))

    def Background_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Background_Image.url))

 

    def __str__(self):
            return 'End_Section_Of_Products'

    class Meta:
         verbose_name_plural = "End_Section_Of_Products"

class Contact(SingleInstanceMixin,models.Model):
    Background_Image = models.ImageField()
    Title = models.CharField(max_length=255)
    Description = models.TextField()

    def Background_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Background_Image.url))



    def __str__(self):
            return 'Contact Us'
    
    class Meta:
         verbose_name_plural = " Contact Us"


class Customer_InfoPage(ZeroInstanceMixin,models.Model):
    FullName = models.CharField(max_length=200,blank=False)
    Phone_Number = PhoneNumberField()
    Email = models.EmailField()
    Subject = models.CharField(max_length=500,blank=False,null=True)
    State = models.CharField(max_length=200,blank=False,null=True)
    Message = models.TextField()
    Sent = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.Email

    class Meta:
         verbose_name_plural = "Customer_InfoPage"

class BrochurePage(models.Model):
    Product_Name = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='static/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product_Name

    class Meta:
         verbose_name_plural = "BrochurePage"
