from django.test import TestCase, Client
from django.urls import reverse
from ..views import home, flights, booking, help


class TestViewsHome(TestCase):

    def test_view_url_accessible_by_name(self):
        # Http request using name
        response = self.client.get(reverse('flightseats-home'))
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_url_exists_at_desired_location(self):
        # Http request using path
        response = self.client.get('/')
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_uses_correct_template(self):
        # Http request using name
        response = self.client.get(reverse('flightseats-home'))
        # check template usage
        self.assertTemplateUsed(response, 'flightseats/home.html', 'Usage of wrong html template!')


class TestViewsFlights(TestCase):

    def test_view_url_accessible_by_name(self):
        # Http request using name
        response = self.client.get(reverse('flights'))
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request has been successfully completed')

    def test_view_url_exists_at_desired_location(self):
        # Http request using path
        response = self.client.get('/flights/')
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request has been successfully completed')

    def test_view_uses_correct_template(self):
        # Http request using name
        response = self.client.get(reverse('flights'))
        # check template usage
        self.assertTemplateUsed(response, 'flightseats/flights.html', 'Usage of wrong html template!')
