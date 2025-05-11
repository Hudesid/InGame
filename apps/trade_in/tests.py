from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class TradeInCreateAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/tradeIn/"
        self.client = APIClient()

    def tradeIn_create_post(self):
        data = {"name": "Test", "phone": "+998111111111", "telegram_nik": "@test", "config": "test"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
