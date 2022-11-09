from django.urls import path
from . import views

app_name = "countries"
urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:idCountry>", views.editCountry, name="editCountry"),
    path("new/", views.newCountries, name="newCountry"),
    path("delete/<int:idCountry>", views.deleteCountry, name="deleteCountry"),
]
