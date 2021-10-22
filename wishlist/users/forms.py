from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Update


class UserUpdateForm(forms.ModelForm):
    firstNameEdit = forms.CharField(label = 'First name', max_length=100)
    lastNameEdit = forms.CharField(label = 'Last name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ['firstNameEdit', 'lastNameEdit', 'username', 'password']
        
class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'password2', 'email']
