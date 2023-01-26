from django.test import TestCase
from django.urls import reverse, resolve
from ..views import home, flights, booking, help


class TestUrls(TestCase):

    def test_home_url_resolve(self):
        url = reverse('flightseats-home')
        self.assertEqual(resolve(url).func, home)

    def test_flights_url_resolve(self):
        url = reverse('flights')
        self.assertEqual(resolve(url).func, flights)

    def test_booking_url_resolve(self):
        url = reverse('booking')
        self.assertEqual(resolve(url).func, booking)

    def test_help_url_resolve(self):
        url = reverse('help')
        self.assertEqual(resolve(url).func, help)
