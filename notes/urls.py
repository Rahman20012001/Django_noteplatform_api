from django.urls import path
from .views import NoteListCreateView, NoteRetrieveUpdateDeleteView, ShareNoteView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDeleteView.as_view(), name='note-retrieve-update-delete'),
    path('notes/<int:pk>/share/', ShareNoteView.as_view(), name='note-share'),
]