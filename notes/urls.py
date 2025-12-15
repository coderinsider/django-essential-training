from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailsView.as_view(), name="notes.detail"),
    path('notes/<int:pk>/share', views.NotePublicDetailView.as_view(), name="notes.public_detail"),
    path('notes/<int:pk>/update', views.NotesUpdatedView.as_view(), name="notes.update"),
    path('notes/<int:pk>/delete', views.NotesDeletedView.as_view(), name="notes.delete"),
    path("notes/new", views.NotesCreateView.as_view(), name="notes.create"),
    path("notes/<int:pk>/add_like", views.add_liked_view, name="notes.add_liked"),
    path("notes/<int:pk>/change_visible_view", views.is_public_view, name="notes.change_visible_view")
]