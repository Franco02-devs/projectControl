from django.contrib import admin
from apps.records.models import *

class LocationAdmin(admin.ModelAdmin):
    list_display=('id','latitude','longitude')

# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(Record)
