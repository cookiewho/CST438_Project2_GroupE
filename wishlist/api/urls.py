from django.urls import path
from django.urls.resolvers import URLPattern
from api.views import *

# # app_name = 'user'

urlpatterns = [
    path('create_users/', create_users, name='create_user_view'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('view_users/', view_users, name='view_users_view'),
    path('view_user/<str:pk>/', view_user, name='view_user_view'),
    path('get_ID/<str:pk>/', get_id, name='get_ID_view'),
    path('update_user/<str:pk>', update_user, name='update_user_view'),
    path('delete_user/<str:pk>', delete_user, name='register_view'),
    path('view_items/', view_items, name='view_items_view'),
    path('view_item_by_id/<str:pk>', view_items_by_id, name='view_item_by_id_view'),
    path('view_userlists/', view_userlists, name='view_userlists_view'),
    path('view_userlists_by_userId/<str:pk>', view_userlist_by_userId, name='view_userlists_by_userId_view'),
    path('view_item_by_userlistID/<str:pk>', view_items_by_userlistID, name='view_item_by_userlistID_view'),
    path('view_items_by_user_id/<str:pk1>/<str:pk2>', view_items_by_user, name='view_items_by_user_id_view'),
    path('view_item_by_user_id/<str:pk1>/<str:pk2>/<str:pk3>', view_item_by_user, name='view_item_by_user_id_view'),
    path('delete_item_by_user/<str:pk1>/<str:pk2>/<str:pk3>', delete_item_by_user, name='delete_item_by_user_view'),
    path('update_item_by_user/<str:pk1>/<str:pk2>/<str:pk3>', update_item_by_user, name='update_item_by_user_view'),
    path('create_item_by_user/<str:pk1>/<str:pk2>/<str:pk3>', create_item_by_user, name='create_item_by_user_view'),
    path('create_item/', create_item, name='create_item_view'),
    path('delete_item/<str:pk>', delete_item, name='delete_item_view'),
    path('update_item/<str:pk>', update_item, name='update_item_view'),
]
