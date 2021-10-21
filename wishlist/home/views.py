from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def home_redirect(request):
    return HttpResponseRedirect("/")