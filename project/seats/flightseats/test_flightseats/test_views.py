from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Book, UserBooking, Seats
from ..views import booking


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


class BookingTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.booked_seats = ["1A", "2B", "3C"]
        for seat in self.booked_seats:
            Book.objects.create(seat_choice=seat)

    def test_invalid_seat_selection(self):
        # Test invalid seat selection
        request = self.factory.post('/booking/', {'seat_choice_row': '4', 'seatletter': 'G'})
        request.user = self.user
        response = booking(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("4G" not in Book.objects.values_list("seat_choice", flat=True))

    def test_valid_seat_selection(self):
        # Test invalid seat selection
        request = self.factory.post('/booking/', {'seat_choice_row': '4', 'seatletter': 'A'})
        request.user = self.user
        response = booking(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("4A" in Book.objects.values_list("seat_choice", flat=True))


