from django.http import HttpResponse
from .models import Animal, Location
from django.views import View
from django.shortcuts import render

def index(request):
    animals = {"animals": Animal.objects.all()}
    return render (request, "cryptids/index.html", animals)

def detail(request, animal_id):
    animal = {"animal": Animal.objects.get(pk=animal_id)}
    return render (request, "cryptids/detail.html" , animal)

def location(request, location_id):
    place = Location.objects.get(pk=location_id)
    animals = place.animal_set.all()
    context = {"location": place, "animals": animals}
    return render (request, "cryptids/location.html", context)

def locations(request):
    locations = {"locations": Location.objects.all()}
    return render (request,"cryptids/locations.html", locations)

def login(request):
    return render (request, "cryptids/login.html")

def register(request):
    return render (request, "cryptids/register.html")

def form(request):
    return render (request, "cryptids/Form.html")

def animals(request):
    animals = {"animals": Animal.objects.all()}
    return render  ( request, "cryptids/animal.html",animals)

def about (request):
    return render (request, "cryptids/About.html")