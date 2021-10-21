from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from rest_framework.exceptions import NotAuthenticated
from .models import UserList, Item
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'password2', 'email']

class ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Item
        fields = ['id', 'name', 'price', 'image', 'category', 'description']


class UserListSerializer(serializers.ModelSerializer):
    user_list = ItemSerializer(many=True)
    # user = UserSerializer(many=True)
    class Meta: 
        model = UserList
        fields = ['id', 'list_name', 'user', 'user_list']

class UserListSerializer2(serializers.ModelSerializer):
    user_list = ItemSerializer(many=True)
    user = UserSerializer(many=True)
    class Meta: 
        model = UserList
        fields = ['id', 'list_name', 'user', 'user_list']
