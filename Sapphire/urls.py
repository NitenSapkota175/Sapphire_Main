from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomePage,name='Home'),
    path('AboutUs/',views.AboutUsPage,name='Aboutus'),
    path('products/',views.ProductPage,name='Product'),
    path('product_type1/<str:pk>',views.ProductType1,name='ProductType1'),
    path('product_type2/<str:pk>',views.ProductType2,name='ProductType2'),
    path('ourwork',views.OurWork,name='Ourwork'),
    path('ContactUs/',views.Contactus,name='contactus'),
    path('Brochure',views.Brochure_Page,name='Brochure'),
    #path('download/<str:filename>', views.download_file,name='DownloadFile'),
    path('download_pdf_file/<str:filename>', views.download_pdf_file,name='downloadPdfFile'),
   
]
