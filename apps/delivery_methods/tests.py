from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class DeliveryMethodListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/delivery-methods/"
        self.client = APIClient()

    def delivery_method_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeliveryMethodRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/delivery-method/{id}"
        self.client = APIClient()

    def delivery_method_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)