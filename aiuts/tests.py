from django.test import TestCase
from .models import Transaction, User
from django.urls import reverse

# Create your tests here.
class UserModelTest(TestCase):
    def test_registration_with_all_information(self):
        response = self.client.post(reverse('aiuts:create_acc'), {"fullname": "Testing01", "password": "Asd,car15"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "afe600a43cea6bdaf6c362905db6b883 has been created!")

        
