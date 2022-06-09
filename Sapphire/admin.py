from django.contrib import admin
from . models import Home
# Register your models here.


class SingleInstanceAdminMixin(object):
   
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        return super(SingleInstanceAdminMixin, self).has_add_permission(request)

class HomeAdmin(SingleInstanceAdminMixin,admin.ModelAdmin):
    model = Home

admin.site.register(Home,HomeAdmin)