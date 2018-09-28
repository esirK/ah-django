from django.test import TestCase

from django.urls import reverse


class BaseTestAPIView(TestCase):
    def setUp(self):
        self.login_url = reverse('authentication:login')
        self.registration_url = reverse('authentication:register')

    def register(self, data):
        return self.client.post(self.registration_url, data=data,
                                content_type='application/json')

    def login(self, data):
        return self.client.post(self.login_url, data=data,
                                content_type='application/json')
