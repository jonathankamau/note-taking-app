from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserProfile(BaseModel, User):

    class Meta:
        db_table = 'users'

    def __str__(self):
        return "User: {}".format(self.user.username)

class Note(BaseModel):
    title = models.CharField(max_length=50)
    org_name = models.CharField(max_length=50)
    purpose = models.TextField(blank=False)
    content = models.TextField(blank=False)
    total_attendance = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting_category = models.CharField(max_length=50)

    class Meta:
        db_table = 'notes'

    def __str__(self):
        return "My Notes: {}".format(self.id)

class MeetingCategory(models.Model):
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    date_modified = models.DateTimeField(default=timezone.now, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'meeting_categories'

    def __str__(self):
        return "Meeting Categories: {}".format(self.id)
