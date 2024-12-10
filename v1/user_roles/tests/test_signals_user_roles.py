from django.test import TestCase
from v1.accounts.models.user import User
from v1.user_roles.models.customer import Customer


class CustomerUserTypeChoice4TestCase(TestCase):

    def test_creation_customer_obj_when_register_user_type_choice_4(self):
        user = User.objects.create_user(
            email="testprofile@user.com",
            password="password",
            first_name="John",
            last_name="Doe",
            type_choice=4,
        )

        customer = Customer.objects.filter(user=user).first()
        self.assertIsNotNone(customer)
