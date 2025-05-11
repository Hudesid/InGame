from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class DesktopListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/desktops/"
        self.client = APIClient()

    def desktop_method_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DesktopRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/desktop/{id}"
        self.client = APIClient()

    def desktop_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)