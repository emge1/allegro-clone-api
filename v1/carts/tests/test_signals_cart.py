from django.test import TestCase
from v1.accounts.models.user import User
from v1.carts.models.cart import Cart
from v1.user_roles.models.customer import Customer


class CartCustomerTestCase(TestCase):

    def test_creation_cart_for_new_customer(self):
        user = User.objects.create_user(
            email="testprofile@user.com",
            password="password",
            first_name="John",
            last_name="Doe",
            type_choice=4,
        )
        customer = Customer.objects.get(user=user)
        cart = Cart.objects.filter(user=customer).first()
        self.assertIsNotNone(cart)
