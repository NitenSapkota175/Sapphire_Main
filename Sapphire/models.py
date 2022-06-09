from pyexpat import model
from django.db import models
from django.core.exceptions import ValidationError




class SingleInstanceMixin(object):
    

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)
        super(SingleInstanceMixin, self).clean()

class Settings(SingleInstanceMixin,models.Model):
    Company_name = models.CharField(max_length=225)
    Main_Logo = models.ImageField()
    
    Office_Address_Title = models.CharField(max_length=225)
    Office_Address = models.CharField(max_length=225)
    Office_Location_Pincode = models.IntegerField()

    Contact_Number_1 = models.IntegerField()
    Contact_Number_2 = models.IntegerField()
    Contact_Number_3 = models.IntegerField()

    Offical_Email_Id = models.EmailField()
    Offical_Information_Email_Id = models.EmailField()

    Facebook_Page_Link = models.CharField(max_length=225)
    Instagram_Page_Link = models.CharField(max_length=225)
    


    Factory_Address_Title = models.CharField(max_length=255)
    Factory_Address = models.CharField(max_length=255)
    Factory_Location_Pincode = models.IntegerField()

    copyright_field = models.CharField(max_length=225)

    Footor_Logo = models.ImageField()

class Home(SingleInstanceMixin,models.Model):
    
    Top_Background_Image = models.ImageField()
    Welcome_Title = models.CharField(max_length=225)
    Welcome_Description = models.TextField()

    What_We_Offer_Title = models.CharField(max_length=225) 
    What_We_Offer_Description = models.TextField()     


