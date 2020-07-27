from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import UserProfile, Note, MeetingCategory

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

class NotesForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100, required=True)
    org_name = forms.CharField(label='Organization Name', max_length=100, required=True)
    purpose = forms.CharField(label='Purpose of the meeting', max_length=100, required=True)
    content = forms.CharField(label='Add your Note here', max_length=500, required=True, widget=forms.Textarea)
    total_attendance = forms.IntegerField(label='Enter the total number of participaants', required=True)

    # categories = [(prop['name'], prop['name']) for prop in MeetingCategory.objects.values('name').distinct()]
    # meeting_category = forms.ChoiceField(label='Select meeting category', required=True, choices=categories)

    class Meta:
        model = Note
        fields = ('title', 'org_name', 'purpose', 'content', 'total_attendance')

