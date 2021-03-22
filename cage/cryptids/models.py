from django.db import models
class Animals(models.Model):
   
    def __str__(self):
        return self.animals_text

class Location(models.Model):
    
    def __str__(self):
        return self.location_text
