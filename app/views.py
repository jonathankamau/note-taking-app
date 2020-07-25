from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import User, Note, MeetingCategory
from django.contrib.auth import login, logout, authenticate
from app.forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form_data = RegistrationForm(request.POST)

        if form_data.is_valid():
            form_data.save()
            password = form_data.cleaned_data.get('password')

            password = form_data.cleaned_data.get('password')
            # user = authenticate(username=username)

            return redirect('login')
    else:
        form_data = RegistrationForm()

    return render(request, 'register.html', {'form': form_data})

def login(request):
    if request.method == 'POST':
        form_data = LoginForm(request.POST)

        if form_data.is_valid():
            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:  
                return redirect('dashboard')
            else:
                return HttpResponse('Invalid Credentials')
    else:
        form_data = LoginForm()


    return render(request, 'login.html', {'form': form_data})

def dashboard(request):

    return render(request, 'register.html')