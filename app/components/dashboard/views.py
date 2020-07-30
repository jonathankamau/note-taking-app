"""
Dashboard class view.

"""
from app.views import *

class DashboardView(View):
    """ Dashboard View Class Edit methods."""

    def __init__(self):

        self.template_form = 'dashboard.html'

    @method_decorator(login_required)
    def get(self, request):

        notes = Note.objects.all().filter(
            user_id=request.user.id).order_by('-date_created')

        context = {
            'notes': notes
        }

        return render(request, self.template_form , context)
        