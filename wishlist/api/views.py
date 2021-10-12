from django import forms
from django.http.response import HttpResponseRedirect
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import *
from .models import UserList, Item
from .forms import ItemUpdateForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# from django.db.models import Q
# from rest_framework.filters import (SearchFilter, OrderingFilter)
# from django_filters.rest_framework import DjangoFilterBackend 

#authentication_classes = (TokenAuthentication,)

# authentication_classes = (TokenAuthentication,)
# permission_classes = [IsAuthenticated]

#[url]/api/register/
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return Response(request.data, status=status.HTTP_200_OK)
            #return redirect('login')
    else: 
        form = UserCreationForm()
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        #return render(request, 'home/home.html', {'form': form, 'title':'Register'})

#[url]/api/login/
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None: 
            if user.is_active:
                login(request, user)
                return Response(request.data, status=status.HTTP_200_OK)

            else: 
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("create a user", status=status.HTTP_400_BAD_REQUEST)

@login_required 
def new_item(request):
    form = ItemUpdateForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        image = form.cleaned_data['image']
        category = form.cleaned_data['category']
        description = form.cleaned_data['description']
        
        item = Item (
            name = name, 
            price = price,
            image = image,
            category = category,
            description = description
        )
        
        item.save()
        messages.success(request, f'Successfully added {item.name}')
        return HttpResponseRedirect('/')
    else: 
        form: ItemUpdateForm(request.POST, instance=request.user)
        print("form not vaild")
        return render(request, 'home/home.html', {'form': form, 'title': 'Add a new Item'})

#[url]/api/user_id/wishlist_id/item_id, add item
#[url]/api/user_id/wishlist_id/item_id, delete item

#[url]/api/view_users/
@api_view(['GET'])
def view_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

#[url]/api/view_user/<id>/  
@api_view(['GET'])
def view_user(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

#[url]/api/create_user/
@api_view(['POST'])
def create_users(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#[url]/api/update_user/<id>/
@api_view(['POST'])
def update_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance = user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

#[url]/api/delete_user/<id>/
@api_view(['DELETE'])
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("User deleted", status=status.HTTP_200_OK)

#[url]/view_items/
@api_view(['GET'])
def view_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#[url]/view_items_by_user_id/<id>/
@api_view(['GET'])
def view_items_by_user(request, id):
    try:
        items = UserList.objects.filter(user=id)
    except UserList.DoesNotExist:
        return Response("User list not found")
    serializer = UserSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#[url]/view_item_by_id/<id>
@api_view(['GET'])
def view_items_by_id(request, pk):
    try:
        items = Item.objects.get(id=pk)
    except:
        return Response("ID not found")
    serializer = ItemSerializer(items, many=False)
    return Response(serializer, status=status.HTTP_200_OK)

#[url]/create_item/
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

#[url]/delete_item/<id>/
@api_view(['DELETE'])
def delete_item (request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response("Item deleted", status=status.HTTP_202_ACCEPTED)

#[url]/update_item/<id>/
@api_view(['POST'])
def update_item(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response("Id not found")
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# #adds an new user to the database url/api/register/. PROBLEM: user is not being vaildated 
# @api_view(['POST'])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data={}
#         if serializer.is_valid():
#             user = serializer.save()
#             data['reponse'] = "successfully registered a new user."
#             data['username'] = user.username
#             data['password'] = user.password
#             data['firstname'] = user.firstname
#             data['lastname'] = user.lastname
#         else:
#             data = serializer.errors
#         return Response(data) 

# class UserList(viewsets.ModelViewSet):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         queryset = User.objects.all()
#         username = self.request.query_params.get('username')
#         if username is not None: 
#             queryset = queryset.filter(username__username=username)
#         return queryset

# @api_view(['GET'])
# def tutorial_list(request):
#     if request.method == 'GET':
#         tutorials = itemList.objects.all()
        
#         # title = request.query_params.get('user_list', None)
#         # if title is not None:
#         #     tutorials = tutorials.filter(user_list=title)
        
#         tutorials_serializer = UserListSerializer(tutorials, many=True)
#         return Response(tutorials_serializer.data)
        # 'safe=False' for objects serialization

    # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'), 
    #         'completed': request.data.get('completed'), 
    #         'user': request.user.id
    #     }
    #     serializer = TodoSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

