from ..models import Book, UserBooking, Seats
from ..views import booking
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User, AnonymousUser
import os


class BookingViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.booked_seat = Book.objects.create(seat_choice='1A')
        self.reservation = UserBooking.objects.create(seat_choice='1A', reserved_by=self.user)
        self.seat_data = Seats.objects.create(column_a='X', column_b='', column_c='', column_d='', column_e='', column_f='', column_g='')

    def test_booking_view_authenticated(self):
        request = self.factory.post('/booking/', {'seat_choice_row': '2', 'seatletter': 'A'})
        request.user = self.user
        response = booking(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['auth_ind'], 'True')


class BookingTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.booked_seats = ["1A", "2B", "3C"]
        for seat in self.booked_seats:
            Book.objects.create(seat_choice=seat)

    def test_booking_authenticated_user(self):
        # Test authenticated user
        request = self.factory.post('/booking/', {'seat_choice_row': '4', 'seatletter': 'D'})
        request.user = self.user
        response = booking(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("4D" in Book.objects.values_list("seat_choice", flat=True))
        self.assertTrue("4D" in UserBooking.objects.values_list("seat_choice", flat=True))
        self.assertEqual(response.context['auth_ind'], "True")
        self.assertEqual(response.context['current_user'], self.user)

    def test_booking_non_authenticated_user(self):
        # Test non-authenticated user
        request = self.factory.post('/booking/', {'seat_choice_row': '4', 'seatletter': 'D'})
        response = booking(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("4D" not in Book.objects.values_list("seat_choice", flat=True))
        self.assertEqual(response.context['auth_ind'], "False")
        self.assertEqual(response.context['current_user'], AnonymousUser())

    def test_invalid_seat_selection(self):
        # WORKING #
        # Test invalid seat selection
        request = self.factory.post('/booking/', {'seat_choice_row': '4', 'seatletter': 'G'})
        request.user = self.user
        response = booking(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("4G" not in Book.objects.values_list("seat_choice", flat=True))

    def test_chartIn_reservations(self):
        request = self.factory.get('/booking/')
        request.user = self.user
        chartIn_reservations = open("flightseats/data/chartIn_reservations.txt", 'r').read()
        self.assertTrue("X" in chartIn_reservations)
        for seat in self.booked_seats:
            self.assertFalse(seat in chartIn_reservations)

    def tearDown(self):
        os.remove("flightseats/data/chartIn_reservations.txt")
        UserBooking.objects.all().delete()
        Book.objects.all().delete()
