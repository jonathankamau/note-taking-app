from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import UserProfile

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='User Name', max_length=100, required=True)
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user

