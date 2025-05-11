from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class LeaveRequestCreateAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/leave-a-request/"
        self.client = APIClient()

    def leave_a_request_create_post(self):
        data = {"name": "Test", "phone": "+998111111111"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
