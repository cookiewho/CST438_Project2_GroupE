"""wishlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls.conf import re_path
from addItems import views as addItems_views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from items import views as item_views
from django.shortcuts import redirect
from rest_framework.authtoken.views import obtain_auth_token
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addItems/', addItems_views.addItems, name='addItems'),
    path('', include('home.urls'), name='home'),
    # re_path(r'^home/$', "views.home-redirect", name="home-redirect"),
    path('', include(('items.urls', 'items'), namespace="items_app")),
    path('items/', item_views.ListAllItems),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login, name='login'),
    path('update/', user_views.update, name='update'),
    path('accountDetails/', user_views.account, name='accountDetails'),

    #REST API URL'S
    path('api/', include('api.urls')),
    
]
