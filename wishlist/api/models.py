from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
        
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default='')
    image = models.URLField(default='')
    category = models.CharField(max_length=100, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name

# List is a list of lists (userList, itemList)
class UserList(models.Model):
    list_name = models.CharField(max_length=100, default='New List')
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    user_list = models.ManyToManyField(Item)