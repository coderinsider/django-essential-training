from typing import List
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView

from .models import Note as Notes
class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'content']
    success_url = "/mynote/notes"
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