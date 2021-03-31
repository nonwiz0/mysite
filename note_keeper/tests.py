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
        # A client request a index page
        response = self.client.get(reverse('note_keeper:index'))
        # A client should receive a normal response code
        self.assertEqual(response.status_code, 200)
        # With there is nothing in the test database, the response should contain the following phrase
        self.assertContains(response, "Your notebook is empty right now!")
        # If there is any available Queryset or variable, it should be empty
        self.assertQuerysetEqual(response.context['latest_note_list'], [])

class Notecreate_noteTests(TestCase):
    def test_create_with_no_title(self):
        # This test is to find whether adding a note with empty title works or not
        # A client click submit button on the form and sent these data to the view
        response = self.client.post(reverse('note_keeper:create_note'), {"title": "", "content": "asdfasdf"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Title or Content is empty, please write the form again")

    def test_create_with_no_content(self):
        # This test to find whether adding a note with empty content giving out any error or not
        response = self.client.post(reverse('note_keeper:create_note'), {"title": "Title Testing 1", "content": ""}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Title or Content is empty, please write the form again")
    
    def test_create_with_same_title(self):
        # This test find out whether the app accepting the same title or not
        response_1 = self.client.post(reverse('note_keeper:create_note'), {"title": "Test", "content": "random content"}, follow=True)
        response_2 = self.client.post(reverse('note_keeper:create_note'), {"title": "Test", "content": "random content testing"}, follow=True)
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        self.assertContains(response_2, "Title is taken, remove the previous note first!")

    def test_create_with_no_title_content(self):
        # This test find out whether adding a note with empty title / body is allow or not
        response = self.client.post(reverse('note_keeper:create_note'), {"title": "", "content": ""}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Title or Content is empty, please write the form again")

    def test_read_an_existing_note(self):
        # Test to see if Notekeeper can read an existing Note
        record = Note.objects.create(title="Diary", content="Making a test")
        record.save()
        response = self.client.get(reverse('note_keeper:note', args=["Diary"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Diary")

    def test_read_an_nonexisting_note(self):
        # Tes to see if Notekeeper cannot read an existing Note
        response = self.client.get(reverse('note_keeper:note', args=["Where is my water?"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Note keeper doesn't have this note")

    def test_read_editing_an_existing_note(self):
        record = Note.objects.create(title="Page Not Found", content="An error that only exist in 20th and 21th century")
        record.save()
        response = self.client.get(reverse('note_keeper:edit_note', args=["Page Not Found"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Page Not Found")

    def test_read_editing_an_non_existing_note(self):
        response = self.client.get(reverse('note_keeper:edit_note', args=["Not existing page"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Note keeper doesn't have this note")

    

    

    def test_update_empty_title_content(self):
        # To update the title, we must first create a record
        record = Note.objects.create(title="Test", content="test")
        record.save()
        # We can try to update it like below here
        response = self.client.post(reverse('note_keeper:update_note'), {"title": "", "content": "", "old_title":"Test"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Title or content is empty, please edit it again")





                
