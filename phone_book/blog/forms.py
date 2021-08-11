from django import forms 

from .models import PhoneNumber

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PhoneForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number','name', 'address']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']