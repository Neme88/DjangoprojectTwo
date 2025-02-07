from operator import itemgetter

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
