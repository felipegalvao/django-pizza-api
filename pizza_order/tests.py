import json
from django.urls import reverse

from rest_framework.test import APITestCase

from pizza_order.models import Pizza
from pizza_order.serializers import PizzaSerializer

class PizzaOrderTestCase(APITestCase):
    url = reverse("pizza_order:list")

    def test_list_pizzas_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_create_pizzas_status_code(self):
        pizza_data = {
            "size": "30",
            "customer_name": "Test Customer",
            "customer_address": "Test Customer Address"
        }
        response = self.client.post(self.url, pizza_data)
        self.assertEqual(201, response.status_code)

    def test_create_pizzas_count(self):
        Pizza.objects.create(
            size="30",
            customer_name="Test Customer 1",
            customer_address="Test Customer Address 1"
        )
        Pizza.objects.create(
            size="50",
            customer_name="Test Customer 2",
            customer_address="Test Customer Address 2"
        )
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Pizza.objects.count())

    def test_create_pizza_with_invalid_size(self):
        pizza_data = {
            "size": "40",
            "customer_name": "Test Customer",
            "customer_address": "Test Customer Address"
        }
        response = self.client.post(self.url, pizza_data)
        self.assertEqual(400, response.status_code)
