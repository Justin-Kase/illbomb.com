from datetime import tzinfo
from illbomb import settings
from merch.models import Merch
from django.contrib import admin

'''
class ReleasesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.release_date = obj.release_date.replace(
            tzinfo=tzinfo.gettz(settings.TIME_ZONE))
        super(ReleasesAdmin, self).save_model(request, obj, form, change)
'''       

admin.site.register(Merch)