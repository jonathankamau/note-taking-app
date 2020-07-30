"""
Notes class view.

"""
from app.views import *

class NoteCreateView(View):
    """ Create Note Class View methods."""

    def __init__(self):

        self.template_form = 'create-note.html'

    @method_decorator(login_required)
    def get(self, request):

        return render(
            request, self.template_form, {'form': NotesForm()}
            )

    @method_decorator(login_required)
    def post(self, request):
        id = request.GET.get('id', None)
        if id is not None:
            note = get_object_or_404(Notes, id=id)
        else:
            note = None

        form_data = NotesForm(request.POST)

        if form_data.is_valid():
            update_user = form_data.save(commit=False)

            update_user.user = request.user
            update_user.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return redirect('dashboard')

        return render(request, self.template_form, {'form': form_data})


class NoteDisplayView(View):
    """ Note Display Class View methods."""

    def __init__(self):

        self.template_form = 'view-note.html'

    @method_decorator(login_required)
    def get(self, request, note_id):
        note = Note.objects.filter(id=note_id)

        context = {'note_details': note}

        return render(request, self.template_form, context)

class NoteSearchView(View):
    """ Note Search Class View methods."""

    def __init__(self):

        self.template_form = 'search_results.html'

    @method_decorator(login_required)
    def get(self, request):
        search_query = request.GET.get('q')

        search_results = Note.objects.filter(
            models.Q(
                user_id=request.user.id, title__icontains=search_query))

        context = {'search_results': search_results}

        return render(request, self.template_form, context)

class NoteFilterView(View):
    """ Note Filter Class View methods."""

    def __init__(self):
        self.template_form = 'filter_results.html'


    @method_decorator(login_required)
    def get(self, request):

        filter_results = self.filter_check(request)

        context = {'filter_results': filter_results}

        return render(request, self.template_form, context)
    
    
    def is_param(self, input):
        return input != '' and input is not None
    

    def filter_check(self, request):
        notes = Note.objects.all().filter(
            user_id=request.user.id)

        org_name = request.GET.get('org_name')
        purpose = request.GET.get('purpose')
        min_attendees = request.GET.get('min_attendees')
        max_attendees = request.GET.get('max_attendees')
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')

        if self.is_param(org_name):
            notes = notes.filter(org_name__iexact=org_name)
        if self.is_param(purpose):
            notes = notes.filter(purpose__iexact=purpose)
        if self.is_param(min_attendees):
            notes = notes.filter(total_attendance__gte=min_attendees)
        if self.is_param(max_attendees):
            notes = notes.filter(total_attendance__lt=max_attendees)
        if self.is_param(from_date):
            notes = notes.filter(date_created__gte=from_date)
        if self.is_param(to_date):
            notes = notes.filter(date_created__lt=to_date)

        return notes


class NoteEditView(View):
    """ Note Class Edit methods."""

    def __init__(self):
        self.template_form = 'edit-note.html'

    @method_decorator(login_required)
    def get(self, request):

        return render(
            request, self.template_form, {'form': NotesForm()}
            )

    @method_decorator(login_required)
    def post(self, request, note_id):
        note = get_object_or_404(Note, id=note_id)

        form_data = NotesForm(request.POST or None, instance=note)

        if form_data.is_valid():
            form_data.save()
            return redirect('dashboard')

        context = {'form': form_data, 'note': note}

        return render(request, self.template_form, context)


