from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class CreditsListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/credits/"
        self.client = APIClient()

    def credit_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreditsRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/credit/{id}"
        self.client = APIClient()

    def credit_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
