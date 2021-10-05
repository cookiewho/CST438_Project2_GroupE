from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserUpdateForm
from users.models import User
from django.contrib.auth.decorators import login_required

def register(request):
  if request.method == 'POST':
    register_form = UserCreationForm(request.POST)
    if register_form.is_valid():
      inputed_username = register_form.cleaned_data.get('username')
      user = User.object.get(username=inputed_username)
      request.session['user_id'] = user.id
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
      authenticated = authenticate(username=inputed_username, password=inputed_password)
      if authenticated is not None:
        user = User.object.get(username=inputed_username)
        # login(request, user)
        request.session['user_id'] = user.id
        messages.info(request, f'Welcome back {inputed_username}.')
        return redirect('admin')
  login_form = AuthenticationForm()
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

def logout(request):
  try:
    del request.session['user_id']
  except KeyError:
    messages.info(request, f'you have been loggeed out!')
    pass
  return render(request, 'home')
