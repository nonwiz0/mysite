from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Note
from django.urls import reverse
from http import HTTPStatus

# Create your tests here.
class NoteIndexViewTests(TestCase):
    def test_no_note(self):
        # If there is no note, an appropriate message is displayed
        response = self.client.get(reverse('note_keeper:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your notebook is empty right now!")
        self.assertQuerysetEqual(response.context['latest_note_list'], [])

class Notecreate_noteTests(TestCase):
    def test_no_title(self):
        response = self.client.post(
                reverse('note_keeper:create_note'), data={"title": "asdfasdfewf23f23f23", "content": "asdfasdf", follow=True}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response, "Title is empty, please add the title")
                
