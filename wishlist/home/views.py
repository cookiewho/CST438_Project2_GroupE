from django.shortcuts import render

posts = [
    {
        'item_no' : '1234',
        'item_name' : 'Harry Potter',
        'content' : 'some small description',
        'publishing_date' : 'September 24, 2021'
    },
    {
        'item_no' : '12345',
        'item_name' : 'Lord of the Rings',
        'content' : 'some small description',
        'publishing_date' : 'September 25, 2021'
    }
]

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

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'home/home.html', context)


def ListAllItems(request):
    # pull from db
    context = {
        'items' : items
    }
    return render(request, 'home/items.html', context)
