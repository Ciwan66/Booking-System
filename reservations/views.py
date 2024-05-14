from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from apartments.models import Apartment, ApartmentImage
from .models import Reservation, ReservationStatus
from datetime import timedelta
from .forms import ReservationForm, UpdateResForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse , reverse_lazy
from django.contrib import messages

from django.views.decorators.http import require_http_methods





# Create your views here.
class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservations/list_res.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user).order_by('-check_in_date')


class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = "reservations/res_detail.html"
    context_object_name = "reservation"

    def get_queryset(self):
        reservations = Reservation.objects.filter(user=self.request.user)
        return reservations

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('error-url'))


class ReservationCreateView(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    template_name = "reservations/res_apt.html"
    redirect_field_name = "next"
    model = Reservation
    success_url = reverse_lazy('list-reserv')
    form_class = ReservationForm
    def get(self, request,**kwargs):
        apartment_id = self.kwargs['pk']
        return HttpResponseRedirect(reverse('detail', args=[apartment_id]))
    def form_invalid(self, form):
        response = super().form_invalid(form)
        apartment_id = self.kwargs['pk']
        messages.error(self.request,"Check dates must be entered")
        return HttpResponseRedirect(reverse('detail', args=[apartment_id]))

    def form_valid(self, form):
        obj = form.save(commit=False)
        apartment_id = self.request.POST.get('apartment')
        if apartment_id:
            apartment_instance = get_object_or_404(Apartment, pk=int(apartment_id))

            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            if check_out_date <= check_in_date:
                messages.error(self.request, "Checkout date must be after check-in date.")
                return HttpResponseRedirect(reverse('detail', args=[apartment_id]))

            reservations = Reservation.objects.filter(
                apartment=apartment_id,
                check_out_date__gte=check_in_date,
                check_in_date__lte=check_out_date,
                reservation_status=ReservationStatus.objects.get(pk=2),
            )
            if reservations:
                messages.error(self.request, "Selected apartment is already booked for the selected dates.")
                return HttpResponseRedirect(reverse('detail', args=[apartment_id]))

            duration_of_stay = check_out_date - check_in_date
            total_price = duration_of_stay.days * apartment_instance.price_per_night

            obj.total_price = total_price
            obj.apartment = apartment_instance

        obj.user = self.request.user
        obj.status = ReservationStatus.objects.get(pk=1)
        return super().form_valid(form)


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = "reservations/update_res.html"
    form_class = UpdateResForm
    success_url = '/res'

    def dispatch(self, request, *args, **kwargs):
        reservation = self.get_object()
        if reservation.user != self.request.user:
            messages.error(self.request, "You are not authorized to update this reservation.")
            return HttpResponseRedirect(reverse('error-url'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        apartment_id = self.request.POST.get('apartment')
        if apartment_id:
            apartment_instance = get_object_or_404(Apartment, pk=int(apartment_id))

            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            if check_out_date <= check_in_date:
                messages.error(self.request, "Checkout date must be after check-in date.")
                return HttpResponseRedirect(reverse('update-reserv', args=[self.object.id]))

            reservations = Reservation.objects.filter(
                apartment=apartment_id,
                check_out_date__gte=check_in_date,
                check_in_date__lte=check_out_date,
                reservation_status=ReservationStatus.objects.get(pk=2),
            )
            if reservations:
                messages.error(self.request, "Selected apartment is already booked.")
                return HttpResponseRedirect(reverse('update-reserv', args=[self.object.id]))

            duration_of_stay = check_out_date - check_in_date
            total_price = duration_of_stay.days * apartment_instance.price_per_night

            obj.total_price = total_price
        obj.status = ReservationStatus.objects.get(pk=1)
        return super().form_valid(form)

@require_http_methods(["POST","GET"])
@user_passes_test(lambda u: u.is_staff, login_url='admin:index')
def apartment_admin(request):
    if request.method == 'POST':
        res_id = request.POST.get('reservation_id')
        new_status = request.POST.get('new_status')
        try:
            res = Reservation.objects.get(id=res_id)
            new_status = ReservationStatus.objects.get(id=new_status)
            res.reservation_status = new_status
            res.save()
            if new_status.id == 2:
                message = f'Hi {res.user.first_name}, your booking request accepted.'
            else:
                message = f'Hi {res.user.first_name}, your booking request rejected'

            subject = 'Booking'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [res.user.email, ]
            send_mail(subject, message, email_from, recipient_list)

        except Reservation.DoesNotExist:
            pass
            return redirect(reverse('test'))

    reservations = Reservation.objects.filter(reservation_status=ReservationStatus.objects.get(pk=1))
    return render(request, 'admin/apartment_admin.html', {'reservations': reservations})

@require_http_methods(["GET", "POST"])
@login_required
def cancel_reservation(request, reservation_id):
    try:
        reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)
        cancel_status = ReservationStatus.objects.get(pk=4)
        reservation.reservation_status = cancel_status
        reservation.save()
        return redirect('detail-reserv', pk=reservation_id)

    except Reservation.DoesNotExist:
        return redirect('error-url')

    except ReservationStatus.DoesNotExist:
        return redirect('error-url')

    except:
        return redirect('error-url')


def redirect_for_errors(request):
    return render(request, 'errors/auth.html')
