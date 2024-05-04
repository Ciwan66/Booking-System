from django.shortcuts import render,redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import Http404


from .models import Apartment,ApartmentImage,Country,City,Category,favorite
from reservations.models import Reservation,ReservationStatus
#import list view
from django.views.generic import ListView, DetailView,View,CreateView,RedirectView,DeleteView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from reservations.forms import ReservationForm
from reviews.models import Comment
#import user to get the user id

class Index(ListView):
    model = Apartment
    template_name = 'index.html'
    context_object_name = 'apartments'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['cities'] = City.objects.all()
        return context
    


# Create your views here.
#  apartment list view content
class ApartmentListView(ListView):
    model = Apartment
    context_object_name = 'apartments'
    template_name = "apartment/list.html"


#  i added the data context to  filter and put the options in the selects to search apartments by country or city...

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'apartments':Apartment.objects.filter(is_active=True),
            'cities': City.objects.all(),
            'countries': Country.objects.all().order_by('country_name'),
                 }
        return context
    
 

#  apartment detil view
class ApartmentDetailView(DetailView):
    
    model = Apartment
    template_name = "apartment/detail.html"
    

    
    
    #get context data to return the images with the detail
    # i returned the images of the apartment also from the apartment image model(table)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        apartment=context['apartment']

        if Reservation.objects.filter(user=self.request.user,apartment=apartment,reservation_status=2):
            context['add_comment'] = True
        else:
            context['add_comment'] = False

        context['comments']=Comment.objects.filter(apartment=apartment)
        context['favorite'] = favorite.objects.filter(apartment=self.object, user=self.request.user).first()

        try:
            images=ApartmentImage.objects.filter(apartment=apartment).order_by('-id')
            context["form"]=ReservationForm
            context["images"]=images
        except ApartmentImage.DoesNotExist:
                pass
                
            
        return context
# search apartment function its have the following fields and i return the apartmens  that matchs these fields

def search_apartments(request):
    country_name=request.GET.get("country_input")
    country_id=request.GET.get("country_id")
    category_id=request.GET.get("category")
    city_name = request.GET.get("city_input")
    city_select = request.GET.get("city_select")
    n_rooms = request.GET.get("n_rooms")
    price_starts = request.GET.get("price_starts")
    price_ends = request.GET.get("price_ends")

    apartments = Apartment.objects.all()

    if country_name:
        # Filter apartments by city name through the related City model
        apartments = apartments.filter(country__country_name__contains=country_name)
    if country_id:
        # Filter apartments by city name through the related City model
        apartments = apartments.filter(country=country_id)
    if category_id:
        # Filter apartments by city name through the related City model
        apartments = apartments.filter(category=category_id)
        
    if city_name:
        # Filter apartments by city name through the related City model
        apartments = apartments.filter(city__city_name__contains=city_name)
    if city_select:
        # Filter apartments by city name through the related City model
        apartments = apartments.filter(city__city_name=city_select)
    if n_rooms:
        apartments = apartments.filter(rooms__gte=n_rooms)
    if  price_starts and price_ends:
        apartments = apartments.filter(price_per_night__range=(price_starts, price_ends))
    elif price_starts:
        apartments = apartments.filter(price_per_night__gte=price_starts)   
    elif price_ends:
        apartments = apartments.filter(price_per_night__lte=price_ends)   
        
    context = {
        'apartments': apartments,
        'cities': City.objects.all(),
        'countries': Country.objects.all().order_by('country_name'),
    }
    
    return render(request, 'apartment/find_apartment.html', context)





class FavoriteCreateView(CreateView):
    model = favorite
    template_name = "apartment/detail.html"
    fields=['apartment']

    def get_success_url(self):
        """Returns the URL to redirect to after a successful form submission."""
        return self.request.POST.get('next', reverse_lazy('home'))

    def form_valid(self, form):
        """If the form is valid, save the associated object."""
        self.object = form.save(commit=False)
        # Assuming you need to set some additional fields before saving
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())

class FavoriteDeleteView(DeleteView):
    model = favorite
    def get_success_url(self):
        """Returns the URL to redirect to after a successful form submission."""
        return self.request.POST.get('next', reverse_lazy('home'))

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())
   
        # Redirect to the detail view of the apartment
 
class FavoriteListView(ListView):
    model = favorite
    template_name = "apartment/user_favorites.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["favorites"] =favorite.objects.filter(user=self.request.user) 
        return context
    
