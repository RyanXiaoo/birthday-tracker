from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from users.forms import registration_form


# Create your views here.
class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/register.html')
    
    def post(self, request, *args, **kwargs):
        form = registration_form()

