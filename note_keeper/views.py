from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Note
from django.utils import timezone
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'note_keeper/index.html'
    context_object_name = 'latest_note_list'

    def get_queryset(self):
        """Return the last five published Note."""
        return Note.objects.order_by('-doc')[:]

class DetailView(generic.DetailView):
    model = Note
    template_name = 'note_keeper/note.html'

class EditView(generic.DetailView):
    model = Note
    template_name = 'note_keeper/edit_note.html'
    
def delete_note(request, note_id):
    Note.objects.filter(pk=note_id).delete()
    return HttpResponseRedirect(reverse('note_keeper:index'))

def create_note(request):
    title = request.POST['title']
    content = request.POST['content']
    note = Note(title=title, content=content, doc=timezone.now())
    note.save()
    return HttpResponseRedirect(reverse('note_keeper:index'))

def update_note(request):
    note_id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']
    
    note = Note.objects.get(pk=note_id)
    note.title = title
    note.content = content 
    note.save()
    return HttpResponseRedirect(reverse('note_keeper:note', args=[note_id]))
