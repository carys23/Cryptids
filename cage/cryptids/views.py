from django.http import HttpResponse
from .models import Animal, Location, Sighting, SightingForm
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView

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
    context = {"locations": Location.objects.all(), "sightings": Sighting.objects.all()}
    
    return render (request,"cryptids/locations.html", context)

def login(request):
    return render (request, "cryptids/login.html")

def register(request):
    return render (request, "cryptids/register.html")

class FormView(TemplateView):
    template_name = "cryptids/Form.html"

    def get(self, request, *args, **kwargs):
        context = {'animals': Animal.objects.all(), 'locations': Location.objects.all()} 

        form = SightingForm()
        context['form'] = form
        return render (request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        receive_form = SightingForm(request.POST)
        context = {'animals': Animal.objects.all(), 'locations': Location.objects.all()} 

        if receive_form.is_valid():
            receive_form.save()
            print("Working")
            return render (request, self.template_name, context)
        else:
            print("Not working")
            form = SightingForm()
            return render (request, self.template_name, context)

    #     animal = Animal.objects.get(name=request.POST.get('animal_name'))
    #     location = Location.objects.get(location_place =request.POST.get('location'))
    #     seen = Sighting(animal=animal,location = location, description =request.POST.get('text'))
    #     seen.save()
    
def animals(request):
    animals = {"animals": Animal.objects.all()}
    return render  ( request, "cryptids/animal.html",animals)

def about (request):
    return render (request, "cryptids/About.html")