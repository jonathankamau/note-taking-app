from django.shortcuts import render, redirect
from app.models import User, Note, MeetingCategory
from django.contrib.auth import login, authenticate
from app.forms import RegistrationForm

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

    return render(request, 'register.html')

def dashboard(request):

    return render(request, 'register.html')