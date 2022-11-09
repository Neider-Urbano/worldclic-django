from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "position")


admin.site.register(Country, CountryAdmin)
