"""
Accounts class based views.
"""

from app.views import *

authentication_form = forms.AuthenticationForm

class RegisterView(View):
    """ Register Class View methods for the signup form."""

    def __init__(self):
        self.template_form = 'register.html'

    def get(self, request):

        return render(request, self.template_form, {'form': RegistrationForm()})

    def post(self, request):
        form_data = RegistrationForm(request.POST)

        if form_data.is_valid():
            user = form_data.save()

            login(request, user)
            return render(request, 'dashboard.html')

        return render(request, self.template_form, {'form': form_data})
    
    

class LoginView(View):
    """ Login Class View methods for the signup form."""

    def __init__(self):
        self.template_form = 'login.html'

    def get(self, request):

        return render(request, self.template_form, {'form': authentication_form()})

    def post(self, request):
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

        return render(request, self.template_form, {'form': form_data})
