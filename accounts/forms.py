from django import forms

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
COMMON_CLASS = 'form-control mb-4'

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
                                                          'class': COMMON_CLASS, 
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
                            widget=forms.TextInput(attrs={'id': 'phoneNumber', 'class': COMMON_CLASS, 'placeholder': 'Phone Number'}))

    class Meta:
        model = CustomUser
        fields =['first_name','last_name','email','password1','password2','phone_number']
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        elif not any(char.isdigit() for char in password1):
            raise ValidationError("Password must contain at least one digit.")
        elif not any(char.isupper() for char in password1):
            raise ValidationError("Password must contain at least one uppercase letter.")
        elif not any(char.islower() for char in password1):
            raise ValidationError("Password must contain at least one lowercase letter.")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords .do not match.")
        return password2


class LoginForm(AuthenticationForm):
    username=forms.EmailField(max_length=50,
                            required=True,
                            widget=forms.EmailInput(attrs={'id':'form2Example11' ,'class':COMMON_CLASS,
                                          'placeholder':'Email address' }))
    password=forms.CharField(max_length=50,
                            required=False,
                            widget=forms.PasswordInput(attrs={'id':"form2Example22", 'class':"form-control",
                                          'placeholder':"Password" }))
    remember_me =forms.BooleanField(required=False)
    class Meta:
        model = CustomUser
        fields = ['username','password','remember_me']
        
    