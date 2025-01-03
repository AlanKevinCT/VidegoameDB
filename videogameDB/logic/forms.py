from django import forms
from .models import Videogame

class Form(forms.ModelForm):
    class Meta:
        model = Videogame
        fields = '__all__'