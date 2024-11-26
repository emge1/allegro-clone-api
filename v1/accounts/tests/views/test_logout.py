from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class LogoutTestCase(APITestCase):

    def setUp(self) -> None:
        User = get_user_model()
        self.user = User.objects.create_user(email="example111@example.com", password="password")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_logout(self):
        response = self.client.post("/logout/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Token.objects.filter(key=self.token.key).exists())
