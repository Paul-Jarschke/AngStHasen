from ..models import Book, UserBooking, Seats
from ..views import booking
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User


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



