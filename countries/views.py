from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Country
from .forms import CountryForm


def index(request):
    context = {
        "countries": Country.objects.all()
    }
    return render(request, "countries/components/list.html", context)


def newCountries(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('countries:index')
    else:
        form = CountryForm()
    context = {'form': form}
    return render(request, "countries/components/new.html", context)


def editCountry(request, idCountry):
    country = Country.objects.get(id=idCountry)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('countries:index')
    else:
        form = CountryForm(instance=country)
    context = {'form': form}
    return render(request, "countries/components/edit.html", context)


def deleteCountry(request, idCountry):
    country = Country.objects.get(id=idCountry)
    country.delete()
    return redirect("countries:index")
