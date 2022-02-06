from django.db.models import fields
from django.forms import ModelForm, ValidationError  
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import User, Grades, Submission

class RegisterForm(UserCreationForm):
    def clean_RA(self):
        print("debug - form validation")
        data = self.cleaned_data['RA']
        print(data)
        print(type(data))
        if not isinstance(data, str):
            raise ValidationError("RA não está no formato RAxxxxx")
        if len(data) < 5:
            raise ValidationError("O tamanho do RA não está correto")
        if not data[:2].isalpha():
            raise ValidationError("Os dois primeiros caracteres devem ser letras (Ex: PC...)")
        if not data[2:].isnumeric():
            raise ValidationError("Após os dois primeiros caracteres o RA deve conter apenas números.")
        return data

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