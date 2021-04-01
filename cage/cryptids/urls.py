from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("animal/<int:animal_id>/", views.detail, name="detail"),
    path("location/<int:location_id>/", views.location, name="location"),
    path("locations/", views.locations, name="locations"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("form/", views.FormView.as_view(), name="form"),
    path("animals/", views.animals, name="animals"),
    path("about/", views.about, name="about")
    
    
]