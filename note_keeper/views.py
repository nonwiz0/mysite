from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Note
from django.utils import timezone
from django.contrib import messages

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'note_keeper/index.html'
    context_object_name = 'latest_note_list'

    def get_queryset(self):
        """Return the last five published Note."""
        return Note.objects.order_by('-modify_date')[:]

class DetailView(generic.DetailView):
    model = Note
    template_name = 'note_keeper/note.html'

class EditView(generic.DetailView):
    model = Note
    template_name = 'note_keeper/edit_note.html'
    
def delete_note(request, note_id):
    messages.info(request, 'Note ID #{} has been deleted'.format(note_id))
    Note.objects.filter(pk=note_id).delete()
    return HttpResponseRedirect(reverse('note_keeper:index'))

def create_note(request):
    title = request.POST['title']
    content = request.POST['content']
    now = timezone.now()
    note = Note(title=title, content=content, doc=now, modify_date=now)
    note.save()
    messages.info(request, 'Note: {} has been saved'.format(title))
    return HttpResponseRedirect(reverse('note_keeper:index'))

def update_note(request):
    note_id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']
    note = Note.objects.get(pk=note_id)

    if note.title == title and note.content == content:
       messages.info(request, "No change detected")
    else:
        note.modify_date = timezone.now()
        note.title = title
        note.content = content 
        note.save()
        messages.info(request, 'Note #{} has been updated'.format(note_id))
    return HttpResponseRedirect(reverse('note_keeper:note', args=[note_id]))
