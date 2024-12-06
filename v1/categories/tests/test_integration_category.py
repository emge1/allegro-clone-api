import pytest
from v1.categories.models.category import Category
from v1.subcategories.models.subcategory import Subcategory
from v1.products.models.product import Product
from rest_framework.test import APITestCase, APIClient


@pytest.mark.django_db
@pytest.mark.integration
class TestCotegoryViews(APITestCase):
    def setUp(self) -> None:
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
            thumbnail="thumbnail44.jpg",
            is_active=True,
            subcategories_id=self.subcategory1
        )

        self.product2 = Product.objects.create(
            name="Product 2",
            max_price=99.99,
            thumbnail="thumbnail5.jpg",
            is_active=True,
            subcategories_id=self.subcategory1
        )

    def test_get_subcategories(self):
        response = self.client.get(f"/categories/{self.category.id}/subcategories")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertEqual(response.json()[0]["title"], "Subcategory 1")
        self.assertEqual(response.json()[0]["thumbnail"], "thumbnail1.jpg")
        self.assertEqual(response.json()[1]["title"], "Subcategory 2")
        self.assertEqual(response.json()[1]["thumbnail"], "thumbnail2.jpg")
        self.assertEqual(response.json()[2]["title"], "Subcategory 3")
        self.assertEqual(response.json()[2]["thumbnail"], "thumbnail3.jpg")

    def test_get_products(self):
        response = self.client.get(f"/categories/{self.category.id}/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.json()[0]["title"], "Product 1")
        self.assertEqual(response.json()[0]["price"], 99.99)
        self.assertEqual(response.json()[0]["thumbnail"], "thumbnail4.jpg")
        self.assertEqual(response.json()[1]["title"], "Product 2")
        self.assertEqual(response.json()[1]["price"], 99.99)
        self.assertEqual(response.json()[1]["thumbnail"], "thumbnail5.jpg")

