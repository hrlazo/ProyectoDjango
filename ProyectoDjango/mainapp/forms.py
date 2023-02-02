from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User #Modelo que va a registrar el formulario
        fields=['username','email','first_name','last_name', 'password1', 'password2' ]#Campos visibiles del formulario
        