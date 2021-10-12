from django.db import models
from django.db.models.deletion import CASCADE
from home.models import List

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.URLField(default='None')
    category = models.CharField(max_length=100, default='None')
    description = models.TextField(default='None')

    def __str__(self):
        return self.name

# List is a list of lists (userList, itemList)
class itemList(models.Model):
    list_name = models.ForeignKey(List, on_delete=CASCADE)
    items = models.ManyToManyField(Item)