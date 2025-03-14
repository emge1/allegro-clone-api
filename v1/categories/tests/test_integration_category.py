import pytest
from v1.categories.models.category import Category
from v1.subcategories.models.subcategory import Subcategory
from v1.products.models.product import Product
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from v1.user_roles.models.merchant import Merchant


@pytest.mark.django_db
@pytest.mark.integration
class TestCategoryViews(APITestCase):
    def setUp(self) -> None:
        User = get_user_model()
        self.user = User.objects.create_user(email="example111@example.com", password="password", type_choice=3)
        self.merchant = Merchant.objects.create(user=self.user)
        self.client = APIClient()
        self.category = Category.objects.create(title="Test category")

        self.subcategory1 = Subcategory.objects.create(
            title="Subcategory 1",
            thumbnail="thumbnail1.jpg",
            is_active=True,
            category=self.category
        )

        self.subcategory2 = Subcategory.objects.create(
            title="Subcategory 2",
            thumbnail="thumbnail2.jpg",
            is_active=True,
            category=self.category
        )

        self.subcategory3 = Subcategory.objects.create(
            title="Subcategory 3",
            thumbnail="thumbnail3.jpg",
            is_active=True,
            category=self.category
        )

        self.product1 = Product.objects.create(
            name="Product 1",
            max_price=99.99,
            thumbnail="thumbnail4.jpg",
            is_active=True,
            subcategories_id=self.subcategory1,
            added_by=self.merchant
        )

        self.product2 = Product.objects.create(
            name="Product 2",
            max_price=99.99,
            thumbnail="thumbnail5.jpg",
            is_active=True,
            subcategories_id=self.subcategory1,
            added_by=self.merchant
        )

    def test_get_subcategories(self):
        response = self.client.get(f"/categories/{self.category.id}/subcategories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        self.assertEqual(response.json()[0]["title"], "Subcategory 1")
        self.assertEqual(response.json()[0]["thumbnail"], "/media/thumbnail1.jpg")
        self.assertEqual(response.json()[1]["title"], "Subcategory 2")
        self.assertEqual(response.json()[1]["thumbnail"], "/media/thumbnail2.jpg")
        self.assertEqual(response.json()[2]["title"], "Subcategory 3")
        self.assertEqual(response.json()[2]["thumbnail"], "/media/thumbnail3.jpg")

    def test_get_products(self):
        response = self.client.get(f"/categories/{self.category.id}/products/")
        print(f"Response JSON: {response.json()}")  # Debuguj odpowiedź API
        print(f"Status Code: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.results.json()), 2)
        self.assertEqual(response.json()[0]["name"], "Product 1")
        self.assertEqual(response.json()[0]["max_price"], '99.99')
        self.assertEqual(response.json()[0]["thumbnail"], "/media/thumbnail4.jpg")
        self.assertEqual(response.json()[1]["name"], "Product 2")
        self.assertEqual(response.json()[1]["max_price"], '99.99')
        self.assertEqual(response.json()[1]["thumbnail"], "/media/thumbnail5.jpg")


