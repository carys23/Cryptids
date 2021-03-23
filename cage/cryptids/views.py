from django.http import HttpResponse
from .models import Animal, Location
from django.views import View

def index(request):
    animals = Animal.objects.all()
    return HttpResponse(animals)

def detail(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(animal)

def place(request, location_id):
    location = Location.objects.get(pk=location_id)
    return HttpResponse(location)

def places(request):
    locations = Location.objects.all()
    return HttpResponse(locations)