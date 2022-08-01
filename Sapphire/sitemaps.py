from django.contrib import sitemaps
from django.urls import reverse
from . models import Product_Type_1 , Product_Type_2 
class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self) :
            return  [
                'Home',
                'Aboutus',
                'Ourwork',
                'Product',
                'contactus'

            ]
    def location(self,item):
        return reverse(item)

class Productsitemap1(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self) :
            return  Product_Type_1.objects.all()
               

        

   
    def location(self, item):
        return reverse('ProductType1', args=[item.id])

class Productsitemap2(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self) :
            return  Product_Type_2.objects.all()
               

    def location(self, item):
        return reverse('ProductType2', args=[item.id])