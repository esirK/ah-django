from authors.apps.authentication.backends import token_decode
from authors.apps.authentication.test.views.base_test import BaseTestAPIView


class TestLoginAPIView(BaseTestAPIView):
    def setUp(self):
        super().setUp()
        self.data = dict(user={
            "username": "Esir",
            "email": "esir@gmail.com",
            "password": "e199407777"})

    def test_non_registered_user_can_not_login(self):
        response = self.login(self.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(response.json().get('errors').get('error')[0],
                         "A user with this email and password was not found.")

    def test_registered_user_can_login(self):
        self.register(self.data)

        response = self.login(self.data)
        self.assertEqual(200, response.status_code)

    def test_wrong_credentials_can_not_login(self):
        self.register(self.data)

        wrong_credentials = dict(user={
            "email": "esir@gmail.com",
            "password": "wrongpass"
        })
        response = self.login(wrong_credentials)

        self.assertEqual(400, response.status_code)
        self.assertEqual(response.json().get('errors').get('error')[0],
                         "A user with this email and password was not found.")

    def test_valid_token_is_returned_on_login(self):
        self.register(self.data)
        response = self.login(self.data)
        self.assertIn("token", response.json().get('user'))
        token = response.json().get('user').get('token')
        decoded_token = token_decode(token)
        self.assertEqual(self.data.get('user').get('email'), decoded_token.get('email'))
