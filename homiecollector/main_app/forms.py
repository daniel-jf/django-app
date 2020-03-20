from django import forms
from django.forms import ModelForm
from .models import Saw
from .models import Homie

class HomieForm(forms.ModelForm):
    class Meta:
        model = Homie
        fields = ('name', 'description', 'age')

class SawForm(ModelForm):
    class Meta:
        model = Saw
        fields = ['date', 'where']