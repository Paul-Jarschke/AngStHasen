from django.test import TestCase
from django.urls import reverse


class TestViewsHome(TestCase):
    """This class checks the view of the home page:

        1) Check if the url is accessible by name.
        2) Check if the url exists at the desired location.
        3) Check if the view uses the correct html template
    """

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
    """This class checks the view of the flights page:

        1) Check if the url is accessible by name.
        2) Check if the url exists at the desired location.
        3) Check if the view uses the correct html template
    """

    def test_view_url_accessible_by_name(self):
        # Http request using name
        response = self.client.get(reverse('flights'))
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_url_exists_at_desired_location(self):
        # Http request using path
        response = self.client.get('/flights/')
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_uses_correct_template(self):
        # Http request using name
        response = self.client.get(reverse('flights'))
        # check template usage
        self.assertTemplateUsed(response, 'flightseats/flights.html', 'Usage of wrong html template!')


class TestViewsHelp(TestCase):
    """This class checks the view of the help page:

        1) Check if the url is accessible by name.
        2) Check if the url exists at the desired location.
        3) Check if the view uses the correct html template
    """

    def test_view_url_accessible_by_name(self):
        # Http request using name
        response = self.client.get(reverse('help'))
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_url_exists_at_desired_location(self):
        # Http request using path
        response = self.client.get('/help/')
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_uses_correct_template(self):
        # Http request using name
        response = self.client.get(reverse('help'))
        # check template usage
        self.assertTemplateUsed(response, 'flightseats/help.html', 'Usage of wrong html template!')


class TestViewsBooking(TestCase):
    """This class checks the view of the booking page:

        1) Check if the url is accessible by name.
        2) Check if the url exists at the desired location.
        3) Check if the view uses the correct html template
    """

    def test_view_url_accessible_by_name(self):
        # Http request using name
        response = self.client.get(reverse('booking'))
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_url_exists_at_desired_location(self):
        # Http request using path
        response = self.client.get('/booking/')
        # check for successful HTTP request
        self.assertEqual(response.status_code, 200, 'HTTP request was unsuccessful!')

    def test_view_uses_correct_template(self):
        # Http request using name
        response = self.client.get(reverse('booking'))
        # check template usage
        self.assertTemplateUsed(response, 'flightseats/booking.html', 'Usage of wrong html template!')
