__author__ = 'cemkiy'
__author__ = 'barisariburnu'

from django import forms
from django.contrib.auth.models import User

class new_member_form(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput)
    email = forms.CharField(max_length=75, widget=forms.TextInput)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, widget=forms.TextInput)
    last_name = forms.CharField(max_length=30, widget=forms.TextInput)

class edit_profile_photo_form(forms.Form):
    profile_photo = forms.ImageField()