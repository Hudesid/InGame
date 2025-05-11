from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class BannerListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/banners/"
        self.client = APIClient()


    def banner_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BannerRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/banner/{id}"
        self.client = APIClient()

    def banner_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)