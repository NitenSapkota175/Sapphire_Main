from django.contrib import admin
from . models import Contact, End_Section_Of_Products, Home,Settings,About,Testimonial,Our_Works,Product_Type_1,Product_Type_2,Product_Type1_Features,Product_Type1_Assurances,Product_Type1_Structure,Product_Type2_Assurance,Product_Type2_Features  
from django.utils.html import format_html
from django.contrib import admin
from django.contrib import admin
class SingleInstanceAdminMixin(object):
   
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        return super(SingleInstanceAdminMixin, self).has_add_permission(request)

class HomeAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = Home
    fields = ['Home_Top_Background_image','Home_Top_Background_Image','Welcome_Title','What_We_Offer_Title','What_We_Offer_Description']
    readonly_fields = ['Home_Top_Background_image']
   
class OurWorkAdmin(admin.ModelAdmin):
    model = Our_Works
    fields = ['image1' , 'Image1' ,'image2' , 'Image2','image3' , 'Image3']
    readonly_fields = ['image1' , 'image2' , 'image3']


class SettingsAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = Settings
    fields = ['Company_Name','Main_logo','Main_Logo' , 'Office_Address_Title' , 'Office_Address1' ,
     'Office_Address2', 'City_1' , 'Office_Address_Zip_Code' , 'Contact_Title', 'Contact_Number_1',
      'Contact_Number_2', 'Contact_Number_3' , 'Email_Title' , 'Offical_Email_Id' , 'Offical_Information_Email_Id' ,
       'Facebook_Page_Link', 'Instagram_Page_Link' , 'Factory_Address_Title', 'Factory_Address1' , 
       'Factory_Address2', 'City_2', 'Factory_Adress_Zip_Code' , 'Copyright_Field', 'Footor_logo' ,
       'Footor_Logo',
        ]
    readonly_fields = ['Main_logo' , 'Footor_logo']

class AboutAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = About
    fields = ['About_Us_Top_Background_image','About_Us_Top_Background_Image','About_Us_Title','About_Us_Description','OurStory_Title','Where_It_All_Began_Title','Where_It_All_Began_Description','Where_It_All_Began_image','Where_It_All_Began_Image','Our_Mission_Title','Testimonial_Title','What_People_Are_Saying_Title']
    readonly_fields = ['About_Us_Top_Background_image','Where_It_All_Began_image']
   
class ContactAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = Contact
    fields = ['Background_image' , 'Background_Image' , 'Title' , 'Description']

    readonly_fields = ['Background_image']

class End_Section_Of_ProductsAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = End_Section_Of_Products
    fields = ['Background_image','Background_Image','Logo1' , 'logo1' , 'Title1', 'Description1' ,'Logo2' , 'logo2' , 'Title2', 'Description2',
        'Logo3' , 'logo3' , 'Title3', 'Description3'
     ]

    readonly_fields = ['Background_image', 'Logo1' , 'Logo2' , 'Logo3']




###################  Products ###########################
class Product_Type1_StructureInline(admin.StackedInline):
    model = Product_Type1_Structure

class Product_Type1_FeaturesInline(admin.StackedInline):
    model = Product_Type1_Features

class Product_Type1_AssurancesInline(admin.StackedInline):
    model = Product_Type1_Assurances

class Product_Type_1Admin(admin.ModelAdmin):
    inlines = [Product_Type1_StructureInline, Product_Type1_FeaturesInline,Product_Type1_AssurancesInline]
    
    fields = ['Product_Name', 'Product_Short_Description_1','Product_Top_Background_image','Product_Top_Background_Image',
    'Product_Short_Description_2','Product_HomePage_Description','Product_ProductPage_Description','Product_Middle_image',
    'Product_Middle_Image','Visit_Our_Website_Title','Website_Link','To_Know_More_Visit_Our_Website',
    'Introduction_Section_Title' , 'Introduction_Section_Description','Introduction_Section_image1',
    'Introduction_Section_Image1','Introduction_Section_image2','Introduction_Section_Image2','Why_Us_Title',
    'Why_Us_Description','Why_Us_image1','Why_Us_Image1','Why_Us_image2','Why_Us_Image2','Why_Us_image3',
    'Why_Us_Image3','Product_Structure_image','Product_Structure_Image']

    readonly_fields = ['Product_Top_Background_image','Product_Middle_image','Introduction_Section_image1',
    'Introduction_Section_image2','Why_Us_image1','Why_Us_image2','Why_Us_image3','Product_Structure_image']


class Product_Type2_FeaturesInline(admin.StackedInline):
    model = Product_Type2_Features

class Product_Type2_AssuranceInline(admin.StackedInline):
    model = Product_Type2_Assurance

class Product_Type_2Admin(admin.ModelAdmin):
    inlines = [ Product_Type2_FeaturesInline,Product_Type2_AssuranceInline]
    fields = ['Product_Name', 'Product_Short_Description_1','Product_Top_Background_image','Product_Top_Background_Image',
    'Product_Short_Description_2','Product_HomePage_Description','Product_ProductPage_Description','Product_Middle_image',
    'Product_Middle_Image','Visit_Our_Website_Title','Website_Link','To_Know_More_Visit_Our_Website',
    'Introduction_Section_Title' , 'Introduction_Section_Description','Introduction_Section_image',
    'Introduction_Section_Image','Why_Us_Title',
    'Why_Us_Description','Why_Us_image1','Why_Us_Image1','Why_Us_image2','Why_Us_Image2',
  ]

    readonly_fields = ['Product_Top_Background_image','Product_Middle_image','Introduction_Section_image',
    'Introduction_Section_Image','Why_Us_image1','Why_Us_image2']




admin.site.register(Settings,SettingsAdmin)
admin.site.register(Home,HomeAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Testimonial)
admin.site.register(Our_Works,OurWorkAdmin)
admin.site.register(Product_Type_1 , Product_Type_1Admin)
admin.site.register(Product_Type_2,Product_Type_2Admin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(End_Section_Of_Products,End_Section_Of_ProductsAdmin)

