from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class SearchAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/search/"
        self.client = APIClient()


    def search_get(self):
        data = {'q': "Something"}
        response = self.client.get(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
