from django.test import TestCase, Client
from django.urls import reverse
from ..views import home, flights, booking, help


class TestViews(TestCase):

    def setUp(self) -> None:
        client = Client()

    def test_home_GET(self):
        response = self.client.get(reverse('list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'flightseats/home.html')

