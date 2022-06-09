from pyexpat import model
from django.db import models
from django.core.exceptions import ValidationError




class SingleInstanceMixin(object):
    

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)
        super(SingleInstanceMixin, self).clean()

class Home(SingleInstanceMixin,models.Model):
    
    Top_Background_Image = models.ImageField()
    Welcome_Title = models.CharField(max_length=225)
    Welcome_Description = models.TextField()

    What_We_Offer_Title = models.CharField(max_length=225) 
    What_We_Offer_Description = models.TextField()     
