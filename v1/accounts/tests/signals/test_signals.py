from django.test import TestCase
from v1.accounts.models.user import User
from v1.accounts.models.profile import Profile


class UserProfileSignalTestCase(TestCase):

    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(
            email="testprofile@user.com",
            password="password",
            first_name="John",
            last_name="Doe"
        )

        profile = Profile.objects.filter(user=user).first()
        self.assertIsNotNone(profile)
