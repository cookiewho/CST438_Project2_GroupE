from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from .models import UserList, Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

        extra_kwargs = {'password': {
            'write_only':True,
            'required':True
        }}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Item
        field = '__all__'

class UserListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta: 
        model = UserList
        field = ('list_name', 'user', 'items')


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
 
#         extra_kwargs = {'password': {
#             'write_only':True,
#             'required':True
#         }}
 
 
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user

# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password2', 'firstname', 'lastname']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def save(self):
#         user = User (
#             username=self.validated_data.get('username', ''),
#             firstname=self.validated_data.get('firstname', ''),
#             lastname=self.validated_data.get('lastname', ''),
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match.'})
#         user.password=password
#         user.save()
#         return user
