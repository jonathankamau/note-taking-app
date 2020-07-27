from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import decorators, forms, login, logout, authenticate
from django.http import HttpResponse
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


def register(request):
    if request.method == 'POST':
        form_data = RegistrationForm(request.POST)

        if form_data.is_valid():
            user = form_data.save()

            login(request, user)
            return render(request, 'dashboard.html')

    else:
        form_data = RegistrationForm()

    return render(request, 'register.html', {'form': form_data})

def user_login(request):
    if request.method == 'POST':
        form_data = authentication_form(data=request.POST)

        if form_data.is_valid():
            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user) 
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('dashboard')
    else:
        form_data = authentication_form()


    return render(request, 'login.html', {'form': form_data})

@login_required
def dashboard(request):
    
    notes = Note.objects.all().filter(
        user_id=request.user.id).order_by('-date_created')

    context = {
        'notes': notes
    }

    return render(request, 'dashboard.html', context)

@login_required
def create_note(request):

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

            update_user.user = request.user
            update_user.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return redirect('dashboard')

    else:
        form_data = NotesForm()

    return render(request, 'create-note.html', {'form': form_data})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    form_data = NotesForm(request.POST or None, instance=note)

    if form_data.is_valid():
        form_data.save()
        return redirect('dashboard')

    context = {'form': form_data, 'note': note}

    return render(request, 'edit-note.html', context)

@login_required
def search_notes(request):

    search_query = request.GET.get('q')

    search_results = Note.objects.filter(
        models.Q(user_id=request.user.id, title__icontains=search_query))

    context = {'search_results': search_results}

    return render(request, 'search_results.html', context)

def is_param(input):
    return input != '' and input is not None

@login_required
def filter_check(request):
    notes = Note.objects.all().filter(
        user_id=request.user.id)

    org_name = request.GET.get('org_name')
    purpose = request.GET.get('purpose')
    min_attendees = request.GET.get('min_attendees')
    max_attendees = request.GET.get('max_attendees')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if is_param(org_name):
        notes = notes.filter(org_name__iexact=org_name)
    if is_param(purpose):
        notes = notes.filter(purpose__iexact=purpose)
    if is_param(min_attendees):
        notes = notes.filter(total_attendance__gte=min_attendees)
    if is_param(max_attendees):
        notes = notes.filter(total_attendance__lt=max_attendees)
    if is_param(from_date):
        notes = notes.filter(date_created__gte=from_date)
    if is_param(to_date):
        notes = notes.filter(date_created__lt=to_date)

    return notes

@login_required
def filter_notes(request):

    filter_results = filter_check(request)

    context = {'filter_results': filter_results}

    return render(request, 'filter_results.html', context)




