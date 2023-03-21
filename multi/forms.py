from django import forms
from django.forms import TextInput,ModelForm
from .models import Todo,Dic,City,User
from django.contrib.auth.forms import UserCreationForm

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

class UserCreation(UserCreationForm):
     class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
        #     widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control my-2'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control my-2'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control my-2'}),
        #     # 'password2': forms.PasswordInput(attrs={'class': 'form-control my-2'}),
            
        # }