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

def place(request, location_id):
    location = {"location": Location.objects.get(pk=location_id)}
    return HttpResponse(location)

def places(request):
    locations = Location.objects.all()
    return HttpResponse(locations)

def login(request):
    return render (request, "cryptids/Home.html")

def register(request):
    return render (request, "cryptids/register.html")

def form(request):
    return render (request, "cryptids/Form.html")
