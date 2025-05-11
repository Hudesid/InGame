from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class CatalogListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/catalogs/"
        self.client = APIClient()

    def catalog_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CatalogRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/catalog/{id}"
        self.client = APIClient()

    def catalog_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
