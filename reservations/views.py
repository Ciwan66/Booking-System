from django.shortcuts import render
from .models import Reservation,ReservationStatus
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from apartments.models import Apartment,ApartmentImage
from datetime import timedelta
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReservationForm,UpdateResForm






# Create your views here.
class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservations/list_res.html'
    context_object_name = 'reservations'


    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user).order_by('-check_in_date')
    
class ReservationDetailView(LoginRequiredMixin,DetailView):
    model = Reservation
    template_name = "reservations/res_detail.html"
    context_object_name = "reservation"  # Your own name for the object that will be passed to the template.

class ReservationCreateView(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    template_name = "reservations/res_apt.html"
    redirect_field_name = "next"
    model = Reservation
    success_url = "/"
    form_class= ReservationForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        apartment_id = self.request.POST.get('apartment')
        if apartment_id:
            apartment_instance = Apartment.objects.get(pk=int(apartment_id))
            
            # Check if checkout date is after check-in date
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            if check_out_date <= check_in_date:
                messages.error(self.request, "Checkout date must be after check-in date.")
                return HttpResponseRedirect(reverse('reservation_create'))  # Redirect to the reservation creation page
            
            # Check if the apartment is available for booking
            if apartment_instance.is_booked:
                messages.error(self.request, "Selected apartment is already booked.")
                return HttpResponseRedirect(reverse('reservation_create'))  # Redirect to the reservation creation page
            
            # Calculate duration of stay
            duration_of_stay = check_out_date - check_in_date
            
            # Calculate total price
            total_price = duration_of_stay.days * apartment_instance.price_per_night
            
            obj.total_price = total_price
            obj.apartment = apartment_instance
        
        obj.user = self.request.user
        obj.status = ReservationStatus.objects.get(pk=1)  # Set default status as New
        return super().form_valid(form)


#creat update list view
class ReservationUpdateView(UpdateView):
    model = Reservation
    template_name = "reservations/update_res.html"
    form_class=UpdateResForm
    success_url='/res'

    def form_valid(self, form):
        obj = form.save(commit=False)
        apartment_id = self.request.POST.get('apartment')
        if apartment_id:
            apartment_instance = Apartment.objects.get(pk=int(apartment_id))
            
            # Check if checkout date is after check-in date
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            if check_out_date <= check_in_date:
                messages.error(self.request, "Checkout date must be after check-in date.")
                return HttpResponseRedirect(reverse('list-reserv'))  # Redirect to the reservation creation page
            
            # Check if the apartment is available for booking
            if apartment_instance.is_booked:
                messages.error(self.request, "Selected apartment is already booked.")
                return HttpResponseRedirect(reverse('list-reserv'))  # Redirect to the reservation creation page
            
            # Calculate duration of stay
            duration_of_stay = check_out_date - check_in_date
            
            # Calculate total price
            total_price = duration_of_stay.days * apartment_instance.price_per_night
            
            obj.total_price = total_price 
        obj.status = ReservationStatus.objects.get(pk=1)  # Set default status as New
        return super().form_valid(form)


