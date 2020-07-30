from django.conf.urls import url
from app.components.notes.views import (
    NoteCreateView, NoteDisplayView, NoteSearchView, NoteFilterView, NoteEditView)


urlpatterns = [
    url(r'^notes/create/$', NoteCreateView.as_view(), name='create_note'),
    url(r'^notes/view/(?P<note_id>\d+)/$', NoteDisplayView.as_view(), name='view_note'),
    url(r'^notes/search_results/$', NoteSearchView.as_view(), name='search_results'),
    url(r'^notes/filter_results/$', NoteFilterView.as_view(), name='filter_results'),
    url(r'^notes/edit/(?P<note_id>\d+)/$', NoteEditView.as_view(), name='edit_note'),
]