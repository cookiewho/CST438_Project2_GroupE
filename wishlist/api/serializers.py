from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from rest_framework.exceptions import NotAuthenticated
from .models import UserList, Item
        
class UserSerializer(serializers.ModelSerializer):
    password2 =serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'password2', 'email']

    def save(self):
        
        
        username = self.validated_data['username']
        for user_in_db in User.objects.all():
            print("AAAAAAH", user_in_db)
            if user_in_db == username:
                raise serializers.ValidationError({'username': "Username is already taken"})
        user = User(username=username, first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'])
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': "Password must match."})
        user.set_password(password)
        user.save()
        return user
            


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
