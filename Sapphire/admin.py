from django.contrib import admin
from . models import Contact, End_Section_Of_Products, Home,Settings,About,Testimonial,Our_Works,Product_Type_1,Product_Type_2,Product_Type1_Features,Product_Type1_Assurances,Product_Type1_Structure,Product_Type2_Assurance,Product_Type2_Features  
# Register your models here.
from django.utils.html import format_html

class SingleInstanceAdminMixin(object):
   
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        return super(SingleInstanceAdminMixin, self).has_add_permission(request)

class HomeAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = Home

class SettingsAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = Settings

class AboutAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = About

class ContactAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = Contact

class End_Section_Of_ProductsAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = End_Section_Of_Products




###################  Products ###########################
class Product_Type1_StructureInline(admin.StackedInline):
    model = Product_Type1_Structure

class Product_Type1_FeaturesInline(admin.StackedInline):
    model = Product_Type1_Features

class Product_Type1_AssurancesInline(admin.StackedInline):
    model = Product_Type1_Assurances

class Product_Type_1Admin(admin.ModelAdmin):
    inlines = [Product_Type1_StructureInline, Product_Type1_FeaturesInline,Product_Type1_AssurancesInline]


class Product_Type2_FeaturesInline(admin.StackedInline):
    model = Product_Type2_Features

class Product_Type2_AssuranceInline(admin.StackedInline):
    model = Product_Type2_Assurance

class Product_Type_2Admin(admin.ModelAdmin):
    inlines = [ Product_Type2_FeaturesInline,Product_Type2_AssuranceInline]




admin.site.register(Settings,SettingsAdmin)
admin.site.register(Home,HomeAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Testimonial)
admin.site.register(Our_Works)
admin.site.register(Product_Type_1 , Product_Type_1Admin)
admin.site.register(Product_Type_2,Product_Type_2Admin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(End_Section_Of_Products,End_Section_Of_ProductsAdmin)

