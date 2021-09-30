from django.urls import path
from django.urls.resolvers import URLPattern
from users.api.views import api_detail_user_view

app_name = 'users'

urlpatterns = [
    path('user/', api_detail_user_view, name='apiUserView'),
]