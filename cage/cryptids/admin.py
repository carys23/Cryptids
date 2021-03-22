from django.contrib import admin
from .models import Location, Animals

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')

admin.site.register(Animals)
admin.site.register(Location)
# Register your models here.

