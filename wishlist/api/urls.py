from django.urls import path
from django.urls.resolvers import URLPattern
from api.views import *

app_name = 'user'

urlpatterns = [
    path('user/', api_detail_user_view, name='apiUserView'),
    path('register/', registration_view, name="register"),
    path('items/', item_list_view, name="item-list"),
    path('items-detail/<str:pk>', item_detail_view, name="item-detail"),
    path('items-create/', item_create_view, name="item-create"),
]