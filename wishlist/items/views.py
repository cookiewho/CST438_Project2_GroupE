from django.shortcuts import render, redirect
from django.http import response, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from api.models import User, UserList
from django.contrib import messages
from api import views as api

def ListAllItems(request):
    if 'user_id' not in request.session:        
        return redirect ("/login")

    response = api.view_items(request)
    context = {'items' : response.data}

    return render(request, 'items/items.html', context)

def ShowItem(request, item_id):
    user_id = request.session['user_id']
    user_list_resp = api.view_userlist_by_userId(request, user_id)

    userlist_id = user_list_resp.data['id']
    response = api.view_items_by_id(request, item_id)

    context = {'item' : response.data, 'user' : user_id, 'list' : userlist_id}
    return render(request, 'items/item.html', context)

def AddItem(request, item_id, user_id, list_id):
    print("Item:", item_id)
    print("User:", user_id)
    print("List:", list_id)

    response = api.create_item_by_user(request, user_id, list_id, item_id)

    if response.status_code == 200:
        messages.success(request, 'Item Added!')
    else:
        messages.error(request, 'Error: Item can not be added to list.')

    return redirect("/items/{}".format(item_id))
    
def ShowUsersList(request):
    if 'user_id' not in request.session:
        return redirect ("/login")
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    userlist = UserList.objects.get(user=user)

    response = api.view_items_by_user(request, user_id, userlist.id)
    context = {'userlist':response.data}

    return render(request, 'items/userLists.html', context)


# def ShowUsersList(request, user_id, userlist_id):

#     response = api.view_items_by_user(request, user_id, userlist_id)
#     context = {'userlist':response.data}

#     return render(request, 'items/userLists.html', context)