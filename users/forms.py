from django.forms import ModelForm
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone', 'location', 'picture']
