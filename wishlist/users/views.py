from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
  if request.method == 'POST':
    register_form = UserCreationForm(request.POST)
    if register_form.is_valid():
      username = register_form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}!')
      return redirect('admin')
  else:  
    register_form = UserCreationForm()
  return render(request, 'users/register.html', {'register_form': register_form})

def login(request):
  if request.method == 'POST':
    login_form = AuthenticationForm(request, data=request.POST)
    if login_form.is_valid():
      inputed_username = login_form.cleaned_data.get('username')
      inputed_password = login_form.cleaned_data.get('password')
      user = authenticate(username=inputed_username, password=inputed_password)
      if user is not None:
        login(request, user)
        messages.info(request, f'Welcome back {inputed_username}.')
        return redirect('admin')
  login_form = AuthenticationForm()
  return render(request, 'users/login.html', {'login_form': login_form})