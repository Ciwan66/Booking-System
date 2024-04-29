from django.shortcuts import render
from .models import Apartment,ApartmentImage
#import list view
from django.views.generic import ListView, DetailView 
#import user to get the user id



# Create your views here.
class ApartmentListView(ListView):
    model = Apartment
    context_object_name = 'apartments'
    template_name = "apartment/list.html"


class ApartmentDetailView(DetailView):
    model = Apartment
    template_name = "apartment/detail.html"
    
    #get context data to return the images with the detail
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        
        apartment=context['apartment']
        try:
            images=ApartmentImage.objects.filter(apartment=apartment).order_by('-id')
        
            context["images"]=images
        except ApartmentImage.DoesNotExist:
                pass
                
            
        return context
    

