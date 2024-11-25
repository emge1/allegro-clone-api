from rest_framework.test import APITestCase
from rest_framework import status
from v1.accounts.models.user import User
from v1.accounts.models.profile import Profile


class RegistrationTestCase(APITestCase):

    def test_register_user_success(self):
        data = {
            "email": "testuser11@example.com",
            "password": "securepassword123",
            "first_name": "John",
            "last_name": "Doe",
            "type_choice": "1"
        }
        response = self.client.post("/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "User registered successfully!")

        user = User.objects.filter(email="testuser11@example.com").first()
        self.assertIsNotNone(user)

        profile = Profile.objects.filter(user=user).first()
        self.assertIsNotNone(profile)

    def test_register_user_with_existing_email(self):
        User.objects.create_user(
            email="testuser11@example.com",
            password="securepassword123",
            first_name="John",
            last_name="Doe"
        )

        data = {
            "email": "testuser11@example.com",
            "password": "anotherpassword123",
            "first_name": "Jane",
            "last_name": "Smith",
            "type_choice": "2"
        }
        response = self.client.post('/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_register_user_missing_fields(self):
        data = {
            "email": "testuser11@example.com",
        }
        response = self.client.post('/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertIn('first_name', response.data)
        self.assertIn('last_name', response.data)

    def test_profile_creation_after_registration(self):
        data = {
            "email": "testuser2@example.com",
            "password": "securepassword123",
            "first_name": "John",
            "last_name": "Doe",
            "type_choice": "1"
        }
        response = self.client.post('/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(email="testuser2@example.com")
        profile = Profile.objects.filter(user=user).first()
        self.assertIsNotNone(profile)
