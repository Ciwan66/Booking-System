from django.shortcuts import render
#import list view
from django.views.generic import ListView, DetailView 

# Create your views here.
def index(request):
    return render(request, 'apartment/index.html') 