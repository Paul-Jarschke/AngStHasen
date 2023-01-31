from django.test import TestCase
from ..models import Flight, Book, Seats, Statistics


class TestModelsStr(TestCase):
    """This class tests the string representation of different models generated by the '__str__' method."""
    def test_Flight_str(self):
        # Create Flight object
        flight = Flight.objects.create(airline='Angsthasen Flights')
        # Check string representation of class
        self.assertEqual(str(flight), 'Angsthasen Flights')

    def test_Book_str(self):
        # Create Flight object
        book = Book.objects.create(seat_choice='A1')
        # Check string representation of class
        self.assertEqual(str(book), 'A1')

    def test_Seats_str(self):
        # Create Seats object
        seats = Seats.objects.create(column_row_number='1')
        # Check string representation of class
        self.assertEqual(str(seats), '1')


class TestModelsStatistics(TestCase):
    """This class tests the creation of a statistics object and its string representation"""
    def test_Statistics_model(self):
        # Create Statistics object
        self.statistics = Statistics.objects.create()
        # Check string representation
        self.assertEqual(str(self.statistics), 'Statistics object (1)')
