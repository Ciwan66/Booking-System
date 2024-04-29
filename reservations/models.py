from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from apartments.models import Apartment

# Create your models here.
class ReservationStatus(models.Model):
    status_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.status_name

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    reservation_status = models.ForeignKey(ReservationStatus, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Reservation for {self.apartment} by {self.user}"