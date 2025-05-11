from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class ServiceCreateAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/services/"
        self.client = APIClient()

    def service_create_post(self):
        data = {"name": "Test", "phone": "+998111111111", "type": "customer", "price": 100.00, "other_services": "test"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
