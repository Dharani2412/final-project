from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={"username": forms.TextInput(attrs={"class":"form-control"}),
        'email': forms.TextInput(attrs={"class":"form-control"}),
        'password1': forms.TextInput(attrs={'class':'form-input'})}