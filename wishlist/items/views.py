from django.shortcuts import render
from api import views

def ListAllItems(request):
    # pull from db
    context = {}
    
    response = views.view_items(request)
    context = {'items' : response.data}

    return render(request, 'items/items.html', context)