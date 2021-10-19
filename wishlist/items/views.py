from django.http import response, JsonResponse
from django.shortcuts import render
from api import views as api

def ListAllItems(request):    
    response = api.view_items(request)
    context = {'items' : response.data}

    return render(request, 'items/items.html', context)

def ShowItem(request, item_id):
    response = api.view_items_by_id(request, item_id)
    context = {'item':response.data}

    return render(request, 'items/item.html', context) 

def ShowUsersList(request, user_id, userlist_id):
    response = api.view_items_by_user(request, user_id, userlist_id)
    context = {'userlist':response.data}

    return render(request, 'items/userLists.html', context)
