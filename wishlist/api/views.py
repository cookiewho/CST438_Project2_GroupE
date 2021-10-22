from os import stat
from django import forms
from django.http import response
from django.http.response import HttpResponseRedirect
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import *
from .models import UserList, Item
from .forms import ItemUpdateForm
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UsernameField
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
import requests

# from django.db.models import Q
# from rest_framework.filters import (SearchFilter, OrderingFilter)
# from django_filters.rest_framework import DjangoFilterBackend 
    
#[url]/api/view_users/
@api_view(['GET'])
def view_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

#[url]/api/view_user/<id>/  
@api_view(['GET'])
def view_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response("User not found")
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

#[url]/api/create_user/
@api_view(['POST'])
def create_users2(request):
    if request.method == 'POST':
        serializer1 = UserSerializer(data=request.data)
        if serializer1.is_valid():
            #serializer1.save()
            # create_newUserList(request)
            #serializer2 = UserListSerializer2(instance=serializer1, data=request.data)
            # if serializer2.is_valid():    
            #     serializer1.save()
            #     serializer2.save()
            #     return Response(serializer1.data, status=status.HTTP_201_CREATED)
            return Response(serializer1.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST) 

#[url]/api/create_user/
@api_view(['POST'])
def create_users(request):
    if request.method == 'POST':
        serializer1 = UserSerializer(data=request.data)
        if serializer1.is_valid():
            # create_newUserList(request)
            serializer1.save()
            # newUserList = UserList.objects.create(serializer1)
            #newUserList = create_newUserList(serializer1.data)
            # if(newUserList == UserList):
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
            # else:
            #     return Response(status=status.HTTP_400_BAD_REQUEST)
        errors = []
        for key, values in serializer1.errors.items():
            errors = [value[:] for value in values]
        return Response(errors, status=status.HTTP_400_BAD_REQUEST) 

#[url]/api/login/
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        authenticated = authenticate(username=username, password=password)
        if authenticated is not None: 
            user = User.objects.get(username=username)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("Not a vaild username or password", status=status.HTTP_400_BAD_REQUEST)

#[url]/api/logout/
@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        username = request.data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response("User not found", status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

#[url]/api/delete_user/<id>/
@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response("User not found", status=status.HTTP_400_BAD_REQUEST )
    User.objects.get(id=pk).delete()
    return Response(f'User {user.username} deleted. {user.username}', status=status.HTTP_200_OK)

#view all items in Item
#[url]/view_items/
@api_view(['GET'])
def view_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#view item by item_id in Item
#[url]/view_item_by_id/<id>
@api_view(['GET'])
def view_items_by_id(request, pk):
    try:
        items = Item.objects.get(id=pk)
    except:
        return Response("ID not found", status=status.HTTP_400_BAD_REQUEST)
    serializer = ItemSerializer(items, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

#[url]/view_userlists/
@api_view(['GET'])
def view_userlists(request):
    userlist = UserList.objects.all()
    serializer = UserListSerializer(userlist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#view items by userlist_id in Userlist
#[url]/view_items_by_user_id/<id>
@api_view(['GET'])
def view_items_by_userlistID(request, pk):
    try:
        items = UserList.objects.get(id=pk)
    except:
        return Response("ID not found", status=status.HTTP_400_BAD_REQUEST)
    serializer = UserListSerializer(items, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

#view all items in the Userlist by user_id and userlist_id
#[url]/view_items_by_user/<user_id>/<userlist_id>
@api_view(['GET'])
def view_items_by_user(request, pk1, pk2):
    try:
        user = User.objects.get(id=pk1)
        items = UserList.objects.get(id=pk2)
    except:
        return Response("User ID or User_List ID not found", status=status.HTTP_400_BAD_REQUEST)
    serializer = UserListSerializer(items, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

#view a item in the userlist by user_id, userlist_id, and item_id
#[url]/view_items_by_user/<user_id>/<userlist_id>/<item_id>
@api_view(['GET'])
def view_item_by_user(request, pk1, pk2, pk3):
    try:
        user = User.objects.get(id=pk1)
        items = UserList.objects.get(id=pk2)
        item = Item.objects.get(id=pk3)
    except:
        return Response("User_ID or User_List ID or Item is not found", status=status.HTTP_400_BAD_REQUEST)
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

#create a item in the userlist by user_id, userlist_id, and item_id
#[url]/create_item_by_user/<user_id>/<userlist_id>/<item_id>
@api_view(['POST'])
def create_item_by_user(request, pk1, pk2, pk3):
    try:
        user = User.objects.get(id=pk1)
        items = UserList.objects.get(id=pk2)
        item = Item.objects.get(id=pk3)
    except:
        return Response("User_ID or User_List ID is not found", status=status.HTTP_400_BAD_REQUEST)
    items.user_list.add(Item.objects.get(id=pk3))
    return Response(f'Item {item.name} added to user list, {user.username}.', status=status.HTTP_200_OK)

#delete a item in the userlist by user_id, userlist_id, and item_id
#[url]/delete_item_by_user/<user_id>/<userlist_id>/<item_id>
@api_view(['DELETE'])
def delete_item_by_user(request, pk1, pk2, pk3):
    try:
        user = User.objects.get(id=pk1)
        items = UserList.objects.get(id=pk2)
        item = Item.objects.get(id=pk3)
    except:
        return Response("User_ID or User_List ID or Item is not found", status=status.HTTP_400_BAD_REQUEST)
    items.user_list.remove(Item.objects.get(id=pk3))
    return Response(f'Item {item.name} deleted.', status=status.HTTP_200_OK)

#update a item in the userlist by user_id, userlist_id, and item_id
#[url]/update_item_by_user/<user_id>/<userlist_id>/<item_id>
@api_view(['PUT'])
def update_item_by_user(request, pk1, pk2, pk3):
    try:
        user = User.objects.get(id=pk1)
        items = UserList.objects.get(id=pk2)
        item = Item.objects.get(id=pk3)
    except:
        return Response("User_ID or User_List ID or Item is not found", status=status.HTTP_400_BAD_REQUEST)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#[url]/create_item/
@api_view(['POST'])
def create_item(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response("Item NOT created!", status=status.HTTP_400_BAD_REQUEST)

#[url]/delete_item/<id>/
@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response("Item not found", status=status.HTTP_400_BAD_REQUEST)
    item.delete()
    return Response(f'Item {item.name} deleted.', status=status.HTTP_200_OK)

#[url]/update_item/<id>/
@api_view(['PUT'])
def update_item(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response("Item not found", status=status.HTTP_400_BAD_REQUEST)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#[url]/api/update_user/<id>/
@api_view(['POST'])
def update_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance = user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

