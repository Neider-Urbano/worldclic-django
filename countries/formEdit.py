from django import forms
from .models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'description', 'position']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'control'}),
            'description': forms.TextInput(attrs={'class': 'control'}),
            'position': forms.NumberInput(attrs={'class': 'control'}),
        }
