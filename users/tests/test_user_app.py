from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError


class UserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="normal@user.com", password="foo", username="normaluser"
        )
        self.assertEqual(user.email, "normal@user.com")
        self.assertEqual(user.username, "normaluser")
        self.assertFalse(user.is_moderator)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="super@user.com", password="foo", username="superuser"
        )
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertEqual(admin_user.username, "superuser")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_create_user_with_no_username(self):
        User = get_user_model()
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="user@nousername.com", password="foo", username=""
            )

    def test_create_user_with_duplicate_email(self):
        User = get_user_model()
        User.objects.create_user(
            email="duplicate@user.com", password="foo", username="user1"
        )
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                email="duplicate@user.com", password="foo", username="user2"
            )

    def test_create_user_with_duplicate_username(self):
        User = get_user_model()
        User.objects.create_user(
            email="user1@duplicate.com", password="foo", username="duplicate"
        )
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                email="user2@duplicate.com", password="foo", username="duplicate"
            )
