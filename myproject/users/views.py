from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import registration_form


# Create your views here.
def login_view(request):
    return HttpResponse("Hello")

def register(request):
    if request.method == 'POST':
        form = registration_form(request.post)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = registration_form()
    return render(request, 'users/register.html', {'form':form})
