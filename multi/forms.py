from django import forms
from django.forms import TextInput,ModelForm
from .models import Todo,Dic,City

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['item']
        widgets = {'item': TextInput(attrs={'class': 'form-control', 'placeholder':'add a list ....'})}


class DicForm(ModelForm):
    class Meta:
        model = Dic
        fields = ['word']
        widgets = {'word': TextInput(attrs={'class': 'form-control', 'placeholder':'Search for a word'})}


class cityform (ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder':'Enter a city name'})}