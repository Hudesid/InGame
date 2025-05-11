from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class PaymentTypeListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/payments/"
        self.client = APIClient()

    def payment_type_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PaymentTypeRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/payment/{id}"
        self.client = APIClient()

    def payment_type_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
