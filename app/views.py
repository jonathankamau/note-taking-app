from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import decorators, forms, login, logout, authenticate
from django.http import HttpResponse
from app.models import User, Note, MeetingCategory
from app.forms import RegistrationForm, NotesForm

authentication_form = forms.AuthenticationForm()
login_required = decorators.login_required()

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
        form_data = authentication_form(data=request.POST)

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
        form_data = authentication_form()


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

def create_note(request):
    username = request.session['username']
    user = User.objects.get(username=username)

    id = request.GET.get('id', None)
    if id is not None:
        note = get_object_or_404(Notes, id=id)
    else:
        note = None

    if request.method == 'POST':
        form_data = NotesForm(request.POST)
        print(form_data)

        if form_data.is_valid():
            update_user = form_data.save(commit=False)

            update_user.user = user
            update_user.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return redirect('dashboard')

    else:
        form_data = NotesForm()

    return render(request, 'create-note.html', {'form': form_data})

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    form_data = NotesForm(request.POST or None, instance=note)

    if form_data.is_valid():
        form_data.save()
        return redirect('dashboard')

    context = {'form': form_data, 'note': note}

    return render(request, 'edit-note.html', context)
