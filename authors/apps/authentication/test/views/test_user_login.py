from django.test import TestCase
from django.urls import reverse


class TestLoginAPIView(TestCase):
    def setUp(self):
        self.login_url = reverse('authentication:login')

    def test_non_registered_user_can_not_login(self):
        data = dict(user={
            "email": "esir@gmail.com",
            "password": "e199407777"
        })
        response = self.client.post(self.login_url, data=data,
                                    content_type='application/json')
        import ipdb; ipdb.set_trace()
        self.assertEqual(201, response.status_code)
