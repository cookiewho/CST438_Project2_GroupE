from django.shortcuts import render

# Create your views here.
def addItems(request):
    return render(request, 'addItems/addItems.html')