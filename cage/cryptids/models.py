from django.db import models
import datetime
from django.utils import timezone
from django import forms
from django.forms import ModelForm

class Location(models.Model):
    location_place = models.CharField(max_length=200)
    country_place = models.CharField(max_length=20)
    
    def __str__(self):
        return(f"{self.location_place},  {self.country_place}")

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
        return(f"{self.name}, {self.type}")

class Sighting(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return(f"{self.animal}, {self.location}")
    
class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
        labels = {
            'location': 'Location',
            'animal': 'Animal',
            'description': 'Description'
        }


    
        