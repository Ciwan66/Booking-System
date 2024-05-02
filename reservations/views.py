from django.shortcuts import render , redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from apartments.models import Apartment,ApartmentImage
from .models import Reservation,ReservationStatus
from datetime import timedelta
from .forms import ReservationForm,UpdateResForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test , login_required
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages




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

    def get_queryset(self):
        # Only show reservations of the authenticated user
        return Reservation.objects.filter(user=self.request.user)

class ReservationCreateView(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    template_name = "reservations/res_apt.html"
    redirect_field_name = "next"
    model = Reservation
    success_url = "/"
    form_class = ReservationForm

    

    def form_valid(self, form):
        obj = form.save(commit=False)
        apartment_id = self.request.POST.get('apartment')
        if apartment_id:
            apartment_instance = Apartment.objects.get(pk=int(apartment_id))
            
            # Check if checkout date is after check-in date
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            if check_out_date <= check_in_date :
                messages.error(self.request, "Checkout date must be after check-in date.")
                return HttpResponseRedirect(reverse('detail', args=[apartment_id]))  # Redirect to the reservation creation page
            
            # Check if the apartment is available for booking
            reservations = Reservation.objects.filter(
                apartment=apartment_id,
                check_out_date__gte=check_in_date,
                check_in_date__lte=check_out_date,
                reservation_status=2,
                
            )
            if reservations :
                messages.error(self.request, "Selected apartment is already booked for the selected dates.")
                return HttpResponseRedirect(reverse('detail', args=[apartment_id]))  # Redirect to the reservation creation page
            
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
                return HttpResponseRedirect(reverse('update-reserv', args=[self.object.id]))  # Redirect to the reservation creation page
            
            # Check if the apartment is available for booking
            reservations = Reservation.objects.filter(
                apartment=apartment_id,
                check_out_date__gte=check_in_date,
                check_in_date__lte=check_out_date,
                reservation_status=2,
                
            )
            if reservations:
                messages.error(self.request, "Selected apartment is already booked.")
                return HttpResponseRedirect(reverse('update-reserv', args=[self.object.id]))  # Redirect to the reservation creation page
            
            # Calculate duration of stay
            duration_of_stay = check_out_date - check_in_date
            
            # Calculate total price
            total_price = duration_of_stay.days * apartment_instance.price_per_night
            
            obj.total_price = total_price 
        obj.status = ReservationStatus.objects.get(pk=1)  # Set default status as New
        return super().form_valid(form)

@user_passes_test(lambda u: u.is_staff,login_url='admin:index')
def apartment_admin(request):
    if request.method == 'POST':
        res_id = request.POST.get('reservation_id')
        new_status = request.POST.get('new_status')
        try:
            res = Reservation.objects.get(id=res_id)
            new_status = ReservationStatus.objects.get(id=new_status)
            res.reservation_status = new_status
            res.save()
            if new_status.id==2:
                message = f'Hi {res.user.first_name}, your booking request accepted.'
            else:
                message = f'Hi {res.user.first_name}, your booking request rejected'

            subject = 'Booking'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [res.user.email, ]
            send_mail( subject, message, email_from, recipient_list )


        except Reservation.DoesNotExist:
            # Handle case where apartment is not found
            pass
            return redirect(reverse('test'))


    # If request method is GET, retrieve all apartments
    reservations = Reservation.objects.filter(reservation_status=1)
    return render(request, 'reservations/apartment_admin.html', {'reservations': reservations})
# views.py


@login_required
def cancel_reservation(request, reservation_id):
    # Ensure that only the owner of the reservation can cancel it
    reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)
    
    try:
        # Retrieve the 'Cancelled' status object
        cancel_status = ReservationStatus.objects.get(id=4)  # Assuming 4 is the ID for "Cancelled" status
        
        # Set the reservation status to 'Cancelled'
        reservation.reservation_status = cancel_status
        reservation.save()
        
        # Redirect to the reservation detail page
        return redirect('detail-reserv', reservation_id=reservation_id)
    except ReservationStatus.DoesNotExist:
        # Handle the case where the status doesn't exist
        # Redirect the user to an appropriate page or display an error message
        return redirect('error-page')