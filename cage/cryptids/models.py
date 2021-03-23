from django.db import models

import datetime
from django.utils import timezone
class Animals(models.Model):
    animals_text = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.animals_text

    @property
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Location(models.Model):
    Animals = models.ForeignKey(Animals, on_delete=models.CASCADE)
    location_text = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.location_text
