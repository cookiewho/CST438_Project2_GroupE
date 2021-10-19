# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Update

<<<<<<< HEAD
class UserUpdateForm(forms.ModelForm):
    firstNameEdit = forms.CharField(label = 'First name', max_length=100)
    lastNameEdit = forms.CharField(label = 'Last name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ['firstNameEdit', 'lastNameEdit', 'username', 'password']
=======
# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']
>>>>>>> bff547b37003cae805aeca8b6394c5efc39afc09
