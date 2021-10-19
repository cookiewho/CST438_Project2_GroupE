from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from items import views as item_views
from django.shortcuts import redirect
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('userlist/<int:user_id>/<int:userlist_id>', item_views.ShowUsersList, name="show_user_list"),
]