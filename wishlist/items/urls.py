from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from items import views as item_views
from django.shortcuts import redirect
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('items/', item_views.ListAllItems),
    path('items/<int:item_id>', item_views.ShowItem, name="specific_item")
]
