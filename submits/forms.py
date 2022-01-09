from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from .models import User, Grades, Submission

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'RA', 'profile_pic']

