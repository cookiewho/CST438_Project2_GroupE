from django.shortcuts import render

def ListAllItems(request):
    # pull from db
    items = [
        {
            'item_no' : '1',
            'item_name' : 'Water Bottle',
            'content' : 'drink water duh',
        },
        {
            'item_no' : '2',
            'item_name' : 'Phone',
            'content' : 'its a phone, what did you expect?',
        }
    ]

    context = {
        'items' : items
    }
    return render(request, 'items/items.html', context)