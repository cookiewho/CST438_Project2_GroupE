from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('items/', views.ListAllItems, name='items-page')
]
