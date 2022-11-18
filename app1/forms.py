from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        # widgets={"first_name": forms.TextInput(attrs={"class":"form-control"}),
        # 'last_name': forms.TextInput(attrs={"class":"form-control"}),
        # 'email': forms.TextInput(attrs={'class':'form-control'}),
        # }




class createUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        # widgets={"username": forms.TextInput(attrs={"class":"form-control"}),
        # 'email': forms.TextInput(attrs={"class":"form-control"})}