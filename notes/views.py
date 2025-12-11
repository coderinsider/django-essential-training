from django.shortcuts import render
from .models import Note as Notes
from django.http import Http404
# Create your views here.
def list(request):
    all_notes = Notes.objects.all()

    return render(request, 'notes/notes-list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exists on our records")
    return render(request, 'notes/notes-details.html', {'note': note})