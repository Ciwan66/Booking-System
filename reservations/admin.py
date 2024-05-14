from django.contrib import admin
from .models import Reservation , ReservationStatus

admin.site.register(Reservation)
admin.site.register(ReservationStatus)