from django import forms

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    first_name=forms.CharField(max_length=50,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control border-top-0 border-left-0 border-right-0',
                                                          'placeholder':'First Name'}))

    last_name=forms.CharField(max_length=50,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control border-top-0 border-left-0 border-right-0',
                                                          'placeholder':'Last Name'}))

    email=forms.EmailField(max_length=50,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control border-top-0 border-left-0 border-right-0',
                                                          'placeholder':'Email'}))

    password1=forms.CharField(max_length=50,
                            required=True,
                            widget=forms.PasswordInput(attrs={'class':'form-control border-top-0 border-left-0 border-right-0',
                                                          'placeholder':'Password'}))

    password2=forms.CharField(max_length=50,
                            required=True,
                            widget=forms.PasswordInput(attrs={'class':'form-control border-top-0 border-left-0 border-right-0',
                                                          'placeholder':'Confirm Password'}))

    phone_number=forms.CharField(max_length=11,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control border-top-0 border-left-0 border-right-0',
                                                          'placeholder':'Phone Number'}))

    class Meta:
        model = CustomUser
        fields =['first_name','last_name','email','password1','password2','phone_number']