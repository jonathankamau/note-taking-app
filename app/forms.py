from django import forms
from django.contrib.auth.hashers import make_password, check_password
from app.models import UserProfile

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)
    username = forms.CharField(label='User Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Input Password', max_length=100, widget=forms.PasswordInput(), required=True, help_text="Enter your password")
    password2 = forms.CharField(label='Repeat Password', max_length=100, widget=forms.PasswordInput(), required=True, help_text="Enter the same password as before")

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
    
    def clean(self):
        cleaned_data = super().clean()

        password2 = cleaned_data.get('password2 ')

        if self.instance.password and password2:
            if not check_password(password2, self.instance.password):
                self.add_error("password2", "The two password fields must match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100, required=True, help_text="Enter your username")
    password = forms.CharField(label='Input Password', max_length=100, widget=forms.PasswordInput(), required=True, help_text="Enter your password")


    class Meta:
        model = UserProfile
        fields = ('username', 'password')
