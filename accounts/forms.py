from django import forms

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 

class RegisterForm(UserCreationForm):

    first_name=forms.CharField(max_length=50,
                            required=True,
                            widget=forms.TextInput(attrs={'id':"textFirstName" ,
                                                          'class':"form-control signupName mb-4" ,
                                                          'placeholder':"First Name"}))

    last_name=forms.CharField(max_length=50,
                            required=True,
                            widget=forms.TextInput(attrs={'id': 'textLastName', 
                                                          'class': 'form-control signupName mb-4', 
                                                          'placeholder': 'Last Name'}))

    email=forms.EmailField(max_length=50,
                            required=True,
                            widget=forms.TextInput(attrs={'id': 'email', 
                                                          'class': 'form-control mb-4', 
                                                          'placeholder': 'Email address'}))

    password1=forms.CharField(max_length=50,
                            required=True,
                            widget=forms.PasswordInput(attrs={'id': 'password', 
                                                              'class': 'form-control', 
                                                              'placeholder': 'Password'}))

    password2=forms.CharField(max_length=50,
                            required=True,
                            widget=forms.PasswordInput(attrs={'id': 'password', 
                                                              'class': 'form-control', 
                                                              'placeholder': 'Confirm Password'}))

    phone_number=forms.CharField(max_length=11,
                            required=True,
                            widget=forms.TextInput(attrs={'id': 'phoneNumber', 'class': 'form-control mb-4', 'placeholder': 'Phone Number'}))

    class Meta:
        model = CustomUser
        fields =['first_name','last_name','email','password1','password2','phone_number']



class LoginForm(AuthenticationForm):
    username=forms.EmailField(max_length=50,
                            required=True,
                            widget=forms.EmailInput(attrs={'id':'form2Example11' ,'class':'form-control mb-4',
                                          'placeholder':'Email address' }))
    password=forms.CharField(max_length=50,
                            required=False,
                            widget=forms.PasswordInput(attrs={'id':"form2Example22", 'class':"form-control",
                                          'placeholder':"Password" }))
    remember_me =forms.BooleanField(required=False)
    class Meta:
        model = CustomUser
        fields = ['username','password','remember_me']