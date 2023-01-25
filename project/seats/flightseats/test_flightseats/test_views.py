from django.test import TestCase, Client
from django.urls import reverse
from ..views import home, flights, booking, help


class TestViewsHome(TestCase):

    def test_view_url_accessible_by_name(self):
        # get HttpRequest using name
        response = self.client.get(reverse('flightseats-home'))
        # check if HTTP request has been successfully completed
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_url_exists_at_desired_location(self):
        # get HttpResponse using path
        response = self.client.get('/')
        # check if HTTP request has been successfully completed
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('flightseats-home'))
        # get HttpResponse
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')
        self.assertTemplateUsed(response, 'flightseats/home.html', 'Usage of wrong html template')


class TestViewsFlights(TestCase):

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('flights'))

        self.assertEqual(response.status_code, 200, 'HTTP request has been successfully completed')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/flights/')
        self.assertEqual(response.status_code, 200, 'HTTP request has been successfully completed')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('flights'))
        self.assertEqual(response.status_code, 200, 'HTTP request has been successfully completed')
        self.assertTemplateUsed(response, 'flightseats/flights.html', 'Usage of wrong html template')
