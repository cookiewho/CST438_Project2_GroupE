from django.db import models
from django.db.models.fields import AutoField
from django.utils import timezone
from django.contrib.auth.models import User

class List(models.Model): 
    list_num = models.IntegerField()
