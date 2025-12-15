from typing import List
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from .models import Note as Notes
class NotesDeletedView(DeleteView):
    model = Notes
    # fields = ['title', 'content']
    success_url = "/mynote/notes"
    template_name = "notes/note_delete.html"

class NotesUpdatedView(UpdateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = "/mynote/notes"
    form_class = NotesForm    
class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = "/mynote/notes"
    form_class = NotesForm
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes-list.html"

class NotesDetailsView(DetailView):
    model = Notes
    context_object_name = "note"

# class PopularNotesListView(DetailView):
#     model = Notes
#     context_object_name = "notes"
#     template_name = "notes/notes-list.html"
#     queryset = Notes.objects.filter(likes__gte=1)