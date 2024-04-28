from django.shortcuts import render
from .models import Apartment,ApartmentImage
#import list view
from django.views.generic import ListView, DetailView 

# Create your views here.
class ApartmentListView(ListView):
    model = Apartment
    context_object_name = 'apartments'
    template_name = "apartment/list.html"

  