from authors.apps.authentication.test.views.base_test import BaseTestAPIView


class TestRegistrationAPIView(BaseTestAPIView):
    def setUp(self):
        super().setUp()
        self.data = dict(user={
            "username": "Esir",
            "email": "esir@gmail.com",
            "password": "e199407777"})

    def test_un_authenticated_users_can_register(self):
        response = self.client.post(self.registration_url, data=self.data,
                                    content_type='application/json')
        self.assertEqual(201, response.status_code)

    def test_user_can_not_register_twice(self):
        self.client.post(self.registration_url, data=self.data,
                         content_type='application/json')
        response = self.client.post(self.registration_url, data=self.data,
                                    content_type='application/json')
        self.assertEqual(400, response.status_code)
