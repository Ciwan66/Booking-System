from django import forms
from django.forms import DateInput
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': DateInput(attrs={'type': 'date'}),
            'check_out_date': DateInput(attrs={'type': 'date'}),
        }


class UpdateResForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': DateInput(attrs={'type': 'date'}),
            'check_out_date': DateInput(attrs={'type': 'date'}),
        }
