from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class CategoryListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/categories/"
        self.client = APIClient()

    def category_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/category/{id}"
        self.client = APIClient()

    def category_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

