from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomePage,name='Home'),
    path('Aboutus/',views.AboutUsPage,name='Aboutus'),
]

