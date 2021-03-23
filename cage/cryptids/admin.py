from django.contrib import admin
from .models import Location, Animal

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')

admin.site.register(Animal)
admin.site.register(Location)
# Register your models here.

