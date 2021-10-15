from django.contrib import admin

#Register your models here.
from .models import UserList, Item

admin.site.register(UserList)
admin.site.register(Item)