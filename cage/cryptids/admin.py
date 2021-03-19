from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')

admin.site.register(City, CityAdmin)
# Register your models here.

