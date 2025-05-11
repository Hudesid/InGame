from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class BrandListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/brands/"
        self.client = APIClient()

    def brand_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BrandRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/brand/{id}"
        self.client = APIClient()

    def brand_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
