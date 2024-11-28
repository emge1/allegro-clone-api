import requests
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework import status


class TestUpdatePassword(APITestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(email="email@example.com", password="old_password")
        self.url = "/update_password/"

    def test_update_password_success(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {"password": "new_secure_password123"}

        response = client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Success", response.data)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("new_secure_password123"))

    def test_update_password_invalid_password(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {"password": "pass"}

        response = client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("old_password"))

    def test_update_password_missing_password(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {}

        response = client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.user.refresh_from_db()

    def test_update_password_unauthenticated(self):
        client = APIClient()
        data = {"password": "new_secure_password123"}

        response = client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("old_password"))
