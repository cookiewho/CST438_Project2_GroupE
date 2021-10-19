from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default='') #change to number
    image = models.URLField(default='')
    category = models.CharField(max_length=100, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name

# List is a list of lists (userList, itemList)
class UserList(models.Model):
    list_name = models.CharField(max_length=100, default='New List')
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=None)
    user_list = models.ManyToManyField(Item)