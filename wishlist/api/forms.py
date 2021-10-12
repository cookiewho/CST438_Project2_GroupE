from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from .models import *

class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'price',
            'image',
            'category',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'ex. IPHONE', 'label': 'name'}),
            'price': forms.NumberInput(attrs={'label': 'price', 'value': '0', 'min': '0', 'max': '5'}),
            'image': forms.TextInput(attrs={'placeholder': 'Enter URL of an Image', 'label': 'image'}),
            'category': forms.TextInput(attrs={'placeholder': 'electronics', 'label': 'category'}),
            'description': forms.TextInput(attrs={'placeholder': 'NEW IPHONE', 'label': 'description'}),
        }