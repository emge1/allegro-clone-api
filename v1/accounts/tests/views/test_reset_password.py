from rest_framework.test import APITestCase
import uuid
from rest_framework import status
from django.contrib.auth import get_user_model
from v1.accounts.models.reset_password_code import ResetPasswordCode


class TestResetPasswordView(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(email="example@example.com", password="old_password")
        self.reset_password_code = ResetPasswordCode.objects.create(user=self.user, code="7e67f18f-600b-49a5-96ca-7456feb92a34")
        self.url = "/reset_password/"

    def test_reset_password_success(self):
        data = {
            "code": "7e67f18f-600b-49a5-96ca-7456feb92a34",
            "password": "new_secure_password123"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Success", response.data)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("new_secure_password123"))

        self.assertFalse(ResetPasswordCode.objects.filter(code="7e67f18f-600b-49a5-96ca-7456feb92a34").exists())

    def test_reset_password_invalid_code(self):
        data = {
            "code": "7e67f18f-600b-49a5-96ca-7456feb92b34",
            "password": "new_secure_password123"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reset_password_invalid_password(self):
        data = {
            "code": "7e67f18f-600b-49a5-96ca-7456feb92a34",
            "password": "short"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Error", response.data)

    def test_reset_password_missing_fields(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
