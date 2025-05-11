from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class CommentListAndCreateAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/commit-from-clients/"
        self.client = APIClient()


    def comments_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def comment_create_post(self):
        data = {
            "username": "Test",
            "comment_uz": "test",
            "comment_ru": "тест",
            "description_uz": "test description",
            "description_ru": "тест описание",
            "image": "somthing image",
            "video": "something video"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CommentRetrieveAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/commit-from-clients/{id}"
        self.client = APIClient()

    def comment_retrieve_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DesktopCommentListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/desktop-comments/"
        self.client = APIClient()


    def desktop_comments_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductCommentListAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/product-comments/"
        self.client = APIClient()


    def product_comments_list_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)