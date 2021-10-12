from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from items.models import *
from users.models import User, userList, Update
from home.models import *
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import *

#shows all the users in the database(User) url/api/users/
# @api_view(['GET'])
# def api_detail_user_view(request):
#     try:
#         user = User.objects.all()   
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user, many=True)
#         return Response(serializer.data)

#adds an new user to the database url/api/register/. PROBLEM: user is not being vaildated 
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user = serializer.save()
            data['reponse'] = "successfully registered a new user."
            data['username'] = user.username
            data['password'] = user.password
            data['firstname'] = user.firstname
            data['lastname'] = user.lastname
        else:
            data = serializer.errors
        return Response(data) 

#shows all items in the database(Item) url/api/items/
@api_view(['GET'])
def item_list_view(request):

    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

#shows a specific item in the database(Item) url/api/item-detail/{primary key} 
#Example url/api/item-detail/1
@api_view(['GET'])
def item_detail_view(request, pk):

    if request.method == 'GET':
        items = Item.objects.get(id=pk)
        serializer = ItemSerializer(items, many=False)
        return Response(serializer.data)

#creates a new item in the database(Item) url/api/item-create/?name=&price=&image=&category=&description=
#Example: url/api/item-create/?name=laptop&price=100&image=someImage&category=electronics&description=An iphone
@api_view(['POST'])
def item_create_view(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

