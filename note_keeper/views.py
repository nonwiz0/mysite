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
        return Note.objects.order_by('-modify_date')[:3]
      #  return Note.objects.filter(modify_date__lte=timezone.now()).order_by('-modify_date')[:]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_note'] = Note.objects.all()
        return context

class DetailView(generic.DetailView):
    model = Note
    template_name = 'note_keeper/note.html'

class EditView(generic.DetailView):
    model = Note
    template_name = 'note_keeper/edit_note.html'
    
def delete_note(request, note_title):
    messages.info(request, 'Note title #{} has been deleted'.format(note_title))
    Note.objects.filter(pk=note_title).delete()
    return HttpResponseRedirect(reverse('note_keeper:index'))

def create_note(request):
    title = request.POST['title']
    content = request.POST['content']
    for note in Note.objects.all():
        if note.title == title:
            messages.info(request, "Title is taken, please use different one!")
            return HttpResponseRedirect(reverse('note_keeper:index'))

    note = Note(title=title, content=content)
    note.save()
    messages.info(request, 'Note: {} has been saved'.format(title))
    return HttpResponseRedirect(reverse('note_keeper:index'))

def update_note(request):
    title = request.POST['title']
    content = request.POST['content']
    curr_title = request.POST['old_title']
    note = Note.objects.get(pk=curr_title)
    if note.title != title: 
        for db_note in Note.objects.all():
            if db_note.title == title:
                messages.info(request, "Title is taken, please use different one!")
                return HttpResponseRedirect(reverse('note_keeper:note', args=[curr_title])) 
        new_note = Note(title=title, content=content,doc=note.doc)  
        Note.objects.filter(pk=note.title).delete()
        new_note.save()
    elif note.title == title and note.content == content:
         messages.info(request, "No change detected")
    else:
        note.modify_date = timezone.now()
        note.title = title
        note.content = content 
        note.save()
        messages.info(request, 'Note #{} has been updated'.format(title))
    return HttpResponseRedirect(reverse('note_keeper:note', args=[title]))

