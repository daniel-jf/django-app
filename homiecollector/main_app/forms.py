from django import forms
from django.forms import ModelForm
from .models import Saw
from .models import Homie
from .models import Location

class HomieForm(forms.ModelForm):
    class Meta:
        model = Homie
        fields = ('name', 'description', 'age')

class SawForm(ModelForm):
    class Meta:
        model = Saw
        fields = ['date', 'where']

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'detail']