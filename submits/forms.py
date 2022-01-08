from django.db.models import fields
from django.forms import ModelForm
from .models import User, Grades, Submission

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'RA', 'profile_pic']

