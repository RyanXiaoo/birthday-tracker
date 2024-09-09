from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput

class registration_form(UserCreationForm):
    password1 = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label= 'Confirm Password',
        widget= forms.PasswordInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label= 'Email',
        widget= forms.EmailInput(attrs={'class': 'form-control'})
    )
    usable_password = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
        }
        
    
