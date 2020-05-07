from django.forms import ModelForm, TextInput
from .models import city
from django import  forms
class CityForm(ModelForm):
    # name = forms.forms.MultipleChoiceField()

    class Meta:
        model = city
        fields = ['name']
        widgets = {
            'name':TextInput(attrs={'class' : 'input','placholder' : 'Enter City Name'})
        }