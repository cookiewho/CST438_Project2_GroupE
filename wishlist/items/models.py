from django.db import models
from django.db.models.deletion import CASCADE


# List is a list of lists (userList, itemList)
   

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
