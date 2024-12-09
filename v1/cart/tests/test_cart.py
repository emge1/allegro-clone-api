from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from v1.cart.models.cart import Cart


class CartTestCase(APITestCase):
    def setUp(self) -> None:
        User = get_user_model()
        self.user = User.objects.create_user(email="example111@example.com", password="password")
        self.client.login(email="example111@example.com", password="password")

    def test_create_chart(self):
        response = self.client.post('/cart/', {})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Cart.objects.count(), 1)
