from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from ..models import Book
from ..views import booking


class BookingTest(TestCase):
    """This class tests the functionality of the booking function."""
    def setUp(self):
        """Create user and seat data for the following functions."""
        # Create RequestFactory
        self.factory = RequestFactory()
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_seat_selection_invalid_row(self):
        """Test seat selection with and invalid row."""
        # Create booking request and response
        request = self.factory.post('/booking/', {'seat_choice_row': '1000', 'seatletter': 'A'})
        request.user = self.user
        response = booking(request)
        # Check if request was successful
        self.assertEqual(response.status_code, 200)
        # Check that seat choice is not in booked objects
        self.assertTrue("1000G" not in Book.objects.values_list("seat_choice", flat=True))

    def test_seat_selection_invalid_column(self):
        """Test seat selection with and invalid column."""
        # Create booking request and response
        request = self.factory.post('/booking/', {'seat_choice_row': '1', 'seatletter': 'Z'})
        request.user = self.user
        response = booking(request)
        # Check if request was successful
        self.assertEqual(response.status_code, 200)
        # Check that seat choice is not in booked objects
        self.assertTrue("1Z" not in Book.objects.values_list("seat_choice", flat=True))

    def test_valid_seat_selection(self):
        """Test seat selection with valid row and column."""
        # Create booking request and response
        request = self.factory.post('/booking/', {'seat_choice_row': '4', 'seatletter': 'A'})
        request.user = self.user
        response = booking(request)
        # Check if request was successful
        self.assertEqual(response.status_code, 200)
        # Check that seat choice is in booked objects
        self.assertTrue("4A" in Book.objects.values_list("seat_choice", flat=True))