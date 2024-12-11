
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from v1.carts.models.cart import Cart
from v1.user_roles.models.customer import Customer


class CartTestCase(APITestCase):
    def setUp(self) -> None:
        User = get_user_model()
        self.user = User.objects.create_user(
            email="example111@example.com", password="password", type_choice=4
        )
        self.client.login(email="example111@example.com", password="password")

    def test_get_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Customer.objects.filter(user=self.user).exists())
        customer = Customer.objects.get(user=self.user)
        self.assertTrue(Cart.objects.filter(user=customer).exists())
        data = response.json()
        self.assertIn('items', data)
        self.assertEqual(data['user'], customer.user.id)

