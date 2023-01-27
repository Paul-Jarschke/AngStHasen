from django.test import TestCase
from ..models import Flight, Book, Seats, User


class TestModels(TestCase):
    def test_Flight_str(self):
        """Method '__str__' should be equal to airline title"""
        flight = Flight.objects.create(airline='Angsthasen Flights')
        self.assertEqual(str(flight), 'Angsthasen Flights')

    def test_Book_str(self):
        """Method '__str__' should be equal to seat_choice title"""
        book = Book.objects.create(seat_choice='A1')
        self.assertEqual(str(book), 'A1')

    def test_Seat_str(self):  # please check this paul
        """Method '__str__' should be equal to column_rownumber"""
        seats = Seats.objects.create(column_rownumber='1')
        self.assertEqual(str(seats), '1')

    def test_User_str(self):
        """Method '__str__' should be equal to name"""
        user = User.objects.create(name='Paul')
        self.assertEqual(str(user), 'Paul')
