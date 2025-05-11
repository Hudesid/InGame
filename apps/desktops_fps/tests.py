from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class GameListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/games/"
        self.client = APIClient()

    def game_method_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GameRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/game/{id}"
        self.client = APIClient()

    def game_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)