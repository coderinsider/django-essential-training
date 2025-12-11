from django.shortcuts import render
from .models import Note as Notes
# Create your views here.
def list(request):
    all_notes = Notes.objects.all()

    return render(request, 'notes/notes-list.html', {'notes': all_notes})