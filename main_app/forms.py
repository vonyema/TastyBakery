from django.forms import ModelForm
from .models import Ingredient
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  



class OrderForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('serving_size', 'filling','frosting','addons','additional')
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email','password1','password2']