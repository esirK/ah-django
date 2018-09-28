from django.test import TestCase

from authors.apps.authentication.models import User


class TestUser(TestCase):
    """
    Test the User model.
    """
    def test_create_user_creates_a_user_successfully(self):
        all_users = User.objects.count()
        self.assertEqual(0, all_users)
        User.objects.create_user(username="Esir", email="esirkings@gmail.com")
        self.assertEqual(1, User.objects.count())

    def test_create_user_raises_type_error_if_username_is_none(self):
        with self.assertRaises(TypeError):
            User.objects.create_user(email="Esirkings@gmail.com")

    def test_create_user_raises_type_error_if_email_is_not_supplied(self):
        with self.assertRaises(TypeError):
            User.objects.create_user(username="Esir")

    def test_create_superuser_can_create_a_user_successfully(self):
        all_users = User.objects.count()
        self.assertEqual(0, all_users)
        User.objects.create_superuser(username="Admin", email="admin@admin.com", password="admin")
        self.assertEqual(1, User.objects.count())

    def test_create_superuser_raises_type_error_if_password_is_not_supplied(self):
        with self.assertRaises(TypeError):
            User.objects.create_superuser(username="Admin", email="admin@admin.com")
