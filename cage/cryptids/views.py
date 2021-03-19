from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import City

class HomepageView(TemplateView):
    template_name = 'home.html'

class SearchResutlsView(ListView):
    model = City
    template_name = 'Search_results.html'

# Create your views here.
