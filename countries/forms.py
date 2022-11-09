from django import forms
from .models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': "name"}),
            'description': forms.TextInput(attrs={'class': 'input', 'placeholder': "description"}),
            'position': forms.NumberInput(attrs={'class': 'input', 'placeholder': "position"}),
        }
