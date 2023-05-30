from django import forms
from django.core import validators

class Login(forms.Form):
    userName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(8)])