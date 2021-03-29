from django.contrib import admin
from .models import Location, Animal, User

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')

admin.site.register(Animal)
admin.site.register(Location)
admin.site.register(User)
# Register your models here.

