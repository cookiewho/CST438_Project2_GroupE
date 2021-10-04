from django.shortcuts import render
# from models import Item

def ListAllItems(request):
    # pull from db
    items = []


    context = {
        'items' : items
    }
    return render(request, 'items/items.html', context)