from django.test import TestCase
from django.urls import reverse


class TestRegistrationAPIView(TestCase):
    def setUp(self):
        self.registration_url = reverse('authentication:register')

    def test_un_authenticated_users_can_register(self):
        data = {'user':
                {
                    "username": "Esir",
                    "email": "esir@gmail.com",
                    "password": "e199407777"
                }
                }
        response = self.client.post(self.registration_url, data=data,
                                    content_type='application/json')
        self.assertEqual(201, response.status_code)
