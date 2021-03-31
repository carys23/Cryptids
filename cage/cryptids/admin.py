from django.contrib import admin
from .models import Location, Animal, Sighting

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')

admin.site.register(Animal)
admin.site.register(Location)
admin.site.register(Sighting)
# Register your models here.

