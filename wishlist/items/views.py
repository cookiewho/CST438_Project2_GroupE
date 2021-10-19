<<<<<<< HEAD
from django.shortcuts import render, redirect

=======
from django.http import response, JsonResponse
from django.shortcuts import render
>>>>>>> main
from api import views as api

def ListAllItems(request):    
    response = api.view_items(request)
    context = {'items' : response.data}

    return render(request, 'items/items.html', context)

def ShowItem(request, item_id):
    response = api.view_items_by_id(request, item_id)

<<<<<<< HEAD
    request.session['user_id'] = 1
    user_id = request.session['user_id']
    
    context = {'item' : response.data, 'user' : user_id}

    return render(request, 'items/item.html', context)

def AddItem(request, item_id, user_id):
    print(" ==== ENTERED FUNCTION ====")
    
    # call view all user lists
    # iterate and find matching user list with user_id
    # get user_list id
    # call api function to add item to user list

    # response = api.create_item_by_user(request, item_id, user_id)
    context = {'item' : response.data}

    return redirect("/")
=======
    return render(request, 'items/item.html', context)
    
def ShowUsersList(request, user_id, userlist_id):
    response = api.view_items_by_user(request, user_id, userlist_id)
    context = {'userlist':response.data}

    return render(request, 'items/userLists.html', context)
>>>>>>> main
