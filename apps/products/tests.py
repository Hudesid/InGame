from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class ProductListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/products/"
        self.client = APIClient()

    def product_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/product/{id}"
        self.client = APIClient()

    def product_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
