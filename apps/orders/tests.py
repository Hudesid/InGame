from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class OrderCreateAPITestCase(APITestCase):
    def setUp(self):
        self.url = "api/order/"
        self.client = APIClient()

    def order_method_post(self):
        data = {
                "customer_name": "test",
                "customer_phone": "+998111111111",
                "address": "test",
                "comment": "test",
                "delivery_method": id,
                "total_price": 100.00,
                "products": [
                    {
                        "desktop": id,
                        "quantity": int,
                        "credit": id,
                        "credit_term": int,
                        "edit_product": [id]
                    },
                    {
                        "product": id,
                        "quantity": int,
                        "credit": id,
                        "credit_term": int,
                    }
                ]
                }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
