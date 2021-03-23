from django.shortcuts import render
from django.http import HttpResponse
from .models import Animals, Location
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse




def detail(render, animals_id):
    animals = get_objects_or_404(Animals, pk=animals_id)
    return render(request, 'animals/detail.html', {'animals': animals})

def index(request):
    context ={"animlas": Animlas.objects.all()}
    return render(request, "animals/index.html", context)

# Create your views here.
