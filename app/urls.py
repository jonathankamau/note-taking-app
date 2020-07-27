"""note_taking_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from app import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'accounts/register/$', views.register, name='register'),
    url(r'^accounts/login/$', views.user_login, name='login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^notes/create/$', views.create_note, name='create_note'),
    url(r'^notes/edit/(?P<note_id>\d+)/$', views.edit_note, name='edit_note'),
    url(r'^notes/search_results/$', views.search_notes, name='search_results'),
    url(r'^notes/filter_results/$', views.filter_notes, name='filter_results')
]
