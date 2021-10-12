# from django.db import models
# from django.db.models.deletion import CASCADE
# from django.contrib.auth.models import User
# # from home.models import List

# # if tables need to be updated, change the model,then run python manage.py migrate

# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.FloatField(default='None')
#     image = models.URLField(default='None')
#     category = models.CharField(max_length=100, default='None')
#     description = models.TextField(default='None')

#     def __str__(self):
#         return self.name

# # List is a list of lists (userList, itemList)
# class itemList(models.Model):
#     list_name = models.CharField(max_length=100, default='New List')
#     user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
#     user_list = models.ManyToManyField(Item)
