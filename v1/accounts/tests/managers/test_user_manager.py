from django.contrib.auth import get_user_model
from django.test import TestCase
from v1.accounts.models.user import User
from v1.accounts.managers.user_manager import UserManager


class UserManagerTestCase(TestCase):
    fixtures = ["users.json"]

    def test_create_user(self):
        User = get_user_model()
        self.user = User.objects.create_user(email='email@example.com', password='foo', first_name="Foo",
                                             last_name="Bar")
        user = self.user
        self.assertEqual(user.email, 'email@example.com')
        self.assertEqual(user.first_name, "Foo")
        self.assertEqual(user.last_name, "Bar")
        self.assertTrue(user.type_choice, 4)
        self.assertEqual(user.id, 5)

    def test_get_user(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.email, "admin@email.com")

    def test_update_user(self):
        pass
