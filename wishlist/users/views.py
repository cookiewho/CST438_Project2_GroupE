from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.contrib.auth.decorators import login_required
from api import views as api
from api import urls as calls
from api import serializers as ser
from home.views import home_redirect
from .forms import UserRegisterForm
import json


def register(request):
  register_form = UserRegisterForm()
  api_call = "/api/create_users/"
  if request.method == 'POST':
    response = api.create_users(request)
    if response.status_code != 400:
      json_resp = (response.data)
      print("LOOK OVER HERE:", response.status_code)
      print("LOOK OVER HERE AGAIN:", response.data)
      messages.success(request, f'Account created for {response.data["username"]}')
      return redirect("/login")
    else:
      error_message = ""
      print("ERROR MESSAGE!:", response.data)
      for val in response.data:
        error_message += val
      return render(request, 'users/register.html', {'register_form': register_form, 'error_message': error_message})
  return render(request, 'users/register.html', {'register_form': register_form})

def login(request):
  login_form = AuthenticationForm()
  if request.method == 'POST':
    response = api.login(request)
    print("LOOK OVER HERE:", response.status_code)
    print("LOOK OVER HERE AGAIN:", response.data)
    if response.status_code != 400:
      json_resp = (response.data)
      request.session['user_id'] = json_resp['id']
      messages.success(request, f'Welcome back {response.data["username"]}!')
      return redirect("/items")
    else:
      error_message = ""
      print("ERROR MESSAGE!:", response.data)
      for val in response.data:
        error_message += val
      return render(request, 'users/login.html', {'login_form': login_form, 'error_message': error_message})  
  return render(request, 'users/login.html', {'login_form': login_form})

@login_required
def update(request):
  if request.method == 'POST':
    update_form = UserUpdateForm(request.POST, instance=request.user)

    if update_form.is_valid:
      update_form.save()
      messages.info(request, f'Your account has been updated!')
      return redirect('update')
  else:
    update_form = UserUpdateForm(instance=request.user)

    context = {
      'update_form': update_form
    }
  
  return render(request, 'users/update.html', context)

@login_required
def account(request):
  if 'user_id' not in request.session:
    return redirect ("/login")
  user_id = request.session['user_id']
  
  if request.method=="POST":
    if 'delete_acc' in request.POST:
      request.method = 'DELETE'
      request.META['REQUEST_METHOD'] = 'DELETE'

      #call api to delete user where user.id == user_id
      response = api.delete_user(request, user_id)
      if response.status_code != 400:
        del request.session['user_id'] # delete session
        messages.success(request, f'Account Deleted, so long space cowboy')
        return redirect('/')
      else:
        messages.error(request, f'Account couldn\'t be deleted, better luck next time!')
        return redirect('/')
    if 'log_out' in request.POST:
      
      del request.session['user_id'] #deleting session
      messages.success(request, f'You have been logged out')
      return redirect('/')
  else:
    response = api.view_user(request, user_id)
    return render(request, 'users/accountDetails.html', response.data)