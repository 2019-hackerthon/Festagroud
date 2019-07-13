from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request, 'festa_home/home.html')

def new(request) :
    return render(request, 'festa_home/new.html'