from django.urls import path
from . import views
app_name ='crydtids'

urlspatterns = [
    path("", views.index, name="index"),
    path("<int:animals_id>/", views.detail, name="detail"),
    ]