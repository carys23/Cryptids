from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("animal/<int:animal_id>/", views.detail, name="detail"),
    path("location/<int:location_id>/", views.place, name="place"),
    path("locations/", views.places, name="places"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("form/", views.form, name="form"),
]