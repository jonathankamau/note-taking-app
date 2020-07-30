from django.contrib import admin
from django.conf.urls import url
from app.modules.account.views import RegisterView, LoginView


urlpatterns = [
    url(r'^accounts/register/$', RegisterView.as_view(), name='register'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
]