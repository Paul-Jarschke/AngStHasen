from django.test import TestCase
from django.urls import reverse, resolve
from ..views import home, flights, booking, help


class TestUrls(TestCase):
    """This class tests URL resolving for different pages."""

    def test_home_url_resolve(self):
        """Tests if the URL named 'flightseats-home' resolves correctly to the 'home' view function."""
        # Generate URl using name
        url = reverse('flightseats-home')
        # Check if URL resolves correctly
        self.assertEqual(resolve(url).func, home)

    def test_flights_url_resolve(self):
        """Tests if the URL named 'flights' resolves correctly to the 'flights' view function."""
        # Generate URl using name
        url = reverse('flights')
        # Check if URL resolves correctly to view function
        self.assertEqual(resolve(url).func, flights)

    def test_booking_url_resolve(self):
        """Tests if the URL named 'booking' resolves correctly to the 'booking' view function."""
        # Generate URl using name
        url = reverse('booking')
        # Check if URL resolves correctly to view function
        self.assertEqual(resolve(url).func, booking)

    def test_help_url_resolve(self):
        """Tests if the URL named 'help' resolves correctly to the 'help' view function."""
        # Generate URl using name
        url = reverse('help')
        # Check if URL resolves correctly to view function
        self.assertEqual(resolve(url).func, help)
