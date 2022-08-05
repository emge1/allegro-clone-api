from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from v1.categories.views.category import CategoryView


class TestCategoryViewCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CategoryView.as_view()
        self.uri = '/categories/'
        self.c = APIClient()

    def test_get_categories(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        print(response)
        self.assertEqual(response.status_code, 200)
