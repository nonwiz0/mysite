from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Note
from django.urls import reverse
from http import HTTPStatus

# Create your tests here.
class NoteIndexViewTests(TestCase):
    def test_read_with_no_note(self):
        # If there is no note, an appropriate message is displayed
        response = self.client.get(reverse('note_keeper:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your notebook is empty right now!")
        self.assertQuerysetEqual(response.context['latest_note_list'], [])

class Notecreate_noteTests(TestCase):
    def test_create_note_with_no_title(self):
        # Testing Create a note without filling the title
        response = self.client.post(reverse('note_keeper:create_note'), {"title": "", "content": "asdfasdf"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response, "Title or Content is empty, please write the form again")
    
    def test_create_note_with_no_content(self):
        # Testing creating a note with title but without content
        response = self.client.post(reverse('note_keeper:create_note'), {"title": "Testing", "content": ""}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response, "Title or Content is empty, please write the form again")
    
    def test_create_note_with_no_title_content(self):
        # Testing creating a note without title / content
        response = self.client.post(reverse('note_keeper:create_note'), {"title": "", "content": ""}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
                response, "Title or Content is empty, please write the form again")
 
    def test_create_note_with_same_title(self):
        # Testing creating a note with the same title
        response = self.client.post(reverse('note_keeper:create_note'), {"title": "Testing", "content": "Content for Testing"}, follow=True)
        sec_response = self.client.post(reverse('note_keeper:create_note'), {"title": "Testing", "content": "Anything"}, follow=True)
        self.assertEqual(sec_response.status_code, 200)
        self.assertContains(
                sec_response, "Title is taken, remove the previous note first!")
    

class Note_Detail_View_test(TestCase):
    def test_read_an_existing_note(self):
        create_note = self.client.post(reverse('note_keeper:create_note'), {"title": "Testing at 1013", "content": "is there bug there?"}, follow=True)
        response = self.client.get(reverse('note_keeper:note', args=["Testing at 1013"]))

    # def test_read_an_nonexisting_note(self):
    #     response = self.client.get(reverse('note_keeper:note', args=["1013"]))
    #     self.assertEqual(response.status_code, 200)

 
    # def test_read_an_unprovided_title(self):
    #     response = self.client.get(reverse('note_keeper:note', args=["1456546"]))
    #     self.assertEqual(response.status_code, 200)

    
class Note_update_note_test(TestCase):
    def test_update_with_provided_title_content(self):
       create_note = self.client.post(reverse('note_keeper:create_note'), {"title": "test1", "content": "content1"}, follow=True)
       response = self.client.post(reverse('note_keeper:update_note'),{"title": "test1", "content": "content1", "old_title": "test1"}, follow=True)
       self.assertEqual(response.status_code, 200)
       self.assertContains(
           response, "No change detected"
       )

    def test_update_with_unprovided_title(self):
        create_note = self.client.post(reverse('note_keeper:create_note'), {"title": "test2", "content": "content is here"}, follow=True)
        response =self.client.post(reverse('note_keeper:update_note'), {"title": " ", "content": "content is here", "old_title": "test2"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
           response, "Sorry, I cannot let you do this"
        )

class Note_delete_note_test(TestCase):
    def test_delete_note(self):
        create_note = self.client.post(reverse('note_keeper:create_note'), {"title": "test1", "content": "content1"}, follow=True)
        response = self.client.post(reverse('note_keeper:delete_note', args=["test1"]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Note title #test1 has been deleted")






