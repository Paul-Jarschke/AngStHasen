from django.test import TestCase, Client
from django.urls import reverse
from ..views import home, flights, booking, help


class TestViewsHome(TestCase):

    def test_view_url_accessible_by_name(self):
        response = self.client.get('flightseats-home')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'flightseats/home.html')


class TestViewsFlights(TestCase):

    def test_view_url_accessible_by_name(self):
        response = self.client.get('flights')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/flights/')
        self.assertEqual(response.status_code, 200)

