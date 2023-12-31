from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Password must contain at least one special character, one number, one capital letter, and one small letter."
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    email1 = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    email2 = forms.EmailField(
        label='Confirm Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    mobile = forms.IntegerField(
        label='Mobile Number',
        widget=forms.TextInput(attrs={'class': 'form-control'}) 

    )
    class Meta:
        model = User
        fields = ['username', 'email1', 'email2', 'password1', 'password2']
        labels = {'email1': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))



class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['name', 'locality', 'city', 'state', 'zipcode']
    widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}), 'city':forms.TextInput(attrs={'class':'form-control'}), 
    'state':forms.Select(attrs={'class':'form-control'}), 'zipcode':forms.NumberInput(attrs={'class':'form-control'})}    
