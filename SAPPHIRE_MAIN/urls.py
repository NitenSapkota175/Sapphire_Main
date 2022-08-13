
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Sapphire.sitemaps import StaticViewsSitemap,Productsitemap1,Productsitemap2
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'sitemap' : StaticViewsSitemap,
    'Product_Type_1' : Productsitemap1,
    'Product_Type_2' : Productsitemap2,

}


urlpatterns = [
    #path('admin/',include('admin_honeypot.urls',namespace='admin_honey')),
    path('sapphire_main_secret_10101111/', admin.site.urls),
    path('',include('Sapphire.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap') #this is straight from django docs
]
#if settings.DEBUG == True:
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
