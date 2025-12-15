from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailsView.as_view(), name="notes.detail"),
    path('notes/<int:pk>/update', views.NotesUpdatedView.as_view(), name="notes.update"),
    path("notes/new", views.NotesCreateView.as_view(), name="notes.create")
]