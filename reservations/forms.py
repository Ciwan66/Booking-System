from django import forms
from django.forms import DateInput
from .models import Reservation , ReservationStatus

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


class ReservationStatusForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    new_status = forms.ModelChoiceField(queryset=ReservationStatus.objects.all(), empty_label=None)