from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from v1.subcategories.views.subcategory import SubcategoryView


class TestSubcategoryViewCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SubcategoryView.as_view()
        self.uri = '/subcategories/'
        self.c = APIClient()

    def test_get_subcategories(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        print(response)
        self.assertEqual(response.status_code, 200)
