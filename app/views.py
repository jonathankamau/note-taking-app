from django.shortcuts import (render, 
                              redirect, get_object_or_404)
from django.utils.decorators import method_decorator
from django.contrib.auth import (decorators, forms, 
                                 login, logout, authenticate)

from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from app.models import User, Note, MeetingCategory, models
from app.forms import RegistrationForm, NotesForm

authentication_form = forms.AuthenticationForm
login_required = decorators.login_required

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'home.html')

def check_for_404(request, exception, template_name="404.html"):
    return render(request, '404.html')
