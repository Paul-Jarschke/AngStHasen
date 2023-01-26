from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User, AnonymousUser
from ..models import Book, Seats, UserBooking
from ..views import booking
import os


class BookingViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.book = Book.objects.create(seat_choice='2A')
        self.reservations = UserBooking.objects.create(
            seat_choice='2A',
            reserved_by=self.user
        )
        self.seats = Seats.objects.create(
            column_a='A',
            column_b='B',
            column_c='C',
            column_d='D',
            column_e='E',
            column_f='F',
            column_g='G'
        )

    def test_booking_view_authenticated(self):
        request = self.factory.post('/booking/', {'seat_choice_row': '2', 'seatletter': 'A'})
        request.user = self.user
        response = booking(request)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context_data['auth_ind'], "True")

        # Check that the 'chartIn_reservations.txt' file is created and contains the booked seat
        self.assertTrue(os.path.isfile('flightseats/data/chartIn_reservations.txt'))
        with open('flightseats/data/chartIn_reservations.txt', 'r') as f:
            contents = f.read()
            print(contents)
            self.assertIn('2A', contents)

    def test_booking_view_unauthenticated(self):
        request = self.factory.get('/booking/')
        request.user = AnonymousUser()
        response = booking(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['auth_ind'], "False")

    def test_booking_view_with_invalid_data(self):
        request = self.factory.post('/booking/', {'seat_choice_row': '1', 'seatletter': 'Z'})
        request.user = self.user
        response = booking(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['auth_ind'], "True")

        # Check that the 'chartIn_reservations.txt' file is created and does not contain the booked seat
        self.assertTrue(os.path.isfile('flightseats/data/chartIn_reservations.txt'))
        with open('flightseats/data/chartIn_reservations.txt', 'r') as f:
            contents = f.read()
            self.assertNotIn('1Z', contents)
