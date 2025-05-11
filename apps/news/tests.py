from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class NewListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/news/"
        self.client = APIClient()

    def new_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NewRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/new/{id}"
        self.client = APIClient()

    def new_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
