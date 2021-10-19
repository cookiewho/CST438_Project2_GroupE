from django.http import response, JsonResponse
from django.shortcuts import render
from api import views as api

def ShowUsersList(request, user_id, userlist_id):
    response = api.view_items_by_user(request, user_id, userlist_id)
    context = {'userlist':response.data}

    return render(request, 'items/userLists.html', context)
