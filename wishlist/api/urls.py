from django.urls import path
from django.urls.resolvers import URLPattern
from api.views import *

# # app_name = 'user'

urlpatterns = [
    path('add_item/', new_item, name='new_item_view'),
    path('create_users/', create_users, name='create_user_view'),
    path('view_users/', view_users, name='view_users_view'),
    path('view_user/<str:pk>/', view_user, name='view_user_view'),
    path('login/', login, name='login_view'),
    path('register/', register, name='register_view'),
    path('update_user/<str:pk>', update_user, name='update_user_view'),
    path('delete_user/<str:pk>', delete_user, name='register_view'),
    path('view_items/', view_items, name='view_items_view'),
    path('view_item_by_user_id/<str:id>', view_items_by_user, name='view_items_by_user_id_view'),
    path('view_item_by_id/<str:pk>', view_items_by_id, name='view_item_by_id_view'),
    path('create_item', create_item, name='create_item_view'),
    path('delete_item/<str:pk>', delete_item, name='delete_item_view'),
    path('update_item/<str:pk>', update_item, name='update_item_view'),

    #path('items/', item_list_view, name="item-list"),
    # path('items-detail/<str:pk>', item_detail_view, name="item-detail"),
    # path('items-create/', item_create_view, name="item-create"),
    #path('items-by-name/', item_by_item_name_view, name="item--by-name"),
]

# from django.conf.urls import url
# from django.urls import path, include
# from .views import (
#     UserSerializer,
# )

# urlpatterns = [
#     #  path('items/', tutorial_list, name='apiUserView'),
# ]

# from django.urls import path, include
# from .views import UserList
# from rest_framework.routers import DefaultRouter
# from rest_framework import viewsets, views
# router = DefaultRouter()
# router.register('articles', ArticleViewSet, basename='articles')
# router.register('users', UserList, basename='users')
 
# urlpatterns = [
 
#     path('users/', views.UserList.as_view(), name='users'),
 
# ]