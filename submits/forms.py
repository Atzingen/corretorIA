from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import User, Grades, Submission

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'RA', 'profile_pic']


class UpdataUserForm(ModelForm):
    username = forms.CharField(max_length=100, required=False)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile_pic']