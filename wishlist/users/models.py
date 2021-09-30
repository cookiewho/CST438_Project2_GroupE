from django.db import models
from django.db.models.deletion import CASCADE
#from home.models import List


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.username