from django.shortcuts import render
from api import views

def ListAllItems(request):
    context = {}
    
    response = views.view_items(request)
    context = {'items' : response.data}

    return render(request, 'items/items.html', context)

def ShowItem(request, item_id):
    print('==== ENTERED FUNCTION ====')
    return render(request, 'items/item.html')