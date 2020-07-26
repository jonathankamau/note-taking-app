from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from app.models import User, Note, MeetingCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from app.forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form_data = RegistrationForm(request.POST)

        if form_data.is_valid():
            form_data.save()
            password = form_data.cleaned_data.get('password')

            return redirect('login')
    else:
        form_data = RegistrationForm()

    return render(request, 'register.html', {'form': form_data})

def login(request):
    if request.method == 'POST':
        form_data = AuthenticationForm(data=request.POST)

        if form_data.is_valid():
            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                request.session['username'] = username  
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('dashboard')
    else:
        form_data = AuthenticationForm()


    return render(request, 'login.html', {'form': form_data})


def dashboard(request):

    username = request.session['username']
    user_id = User.objects.get(username=username).pk
    
    notes = Note.objects.all().filter(user_id=user_id)
    print(notes)

    context = {
        'notes': notes
    }

    return render(request, 'dashboard.html', context)