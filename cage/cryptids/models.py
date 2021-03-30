from django.db import models
import datetime
from django.utils import timezone

class Location(models.Model):
    location_place = models.CharField(max_length=200)
    country_place = models.CharField(max_length=20)
    
    def __str__(self):
        return(f"{self.location_place}, {self.country_place}")

    @property
    def  published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Animal(models.Model):
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    image = models.ImageField(upload_to='upload/')
    description = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return(f"{self.name},{self.type},{self.description}")
        