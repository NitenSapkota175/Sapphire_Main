from django.contrib import admin
from . models import Home,Settings
# Register your models here.


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

admin.site.register(Settings,SettingsAdmin)
admin.site.register(Home,HomeAdmin)