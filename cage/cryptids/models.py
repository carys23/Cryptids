from django.db import models
import datetime
from django.utils import timezone
class Animal(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name

    def __str__(self):
        return self.type
        

class Location(models.Model):
    Animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    location_place = models.CharField(max_length=200)
    country_place = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.location_place

    def __str__(self):
        return self.country_place

    @property
    def  published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)