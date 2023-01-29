from django.test import TestCase
from django.apps import apps
from ..models import Flight


class FlightseatsConfigTest(TestCase):
    """
        This class test different aspects of the FlightseatsConfig class and its ready() function.
    """
    def test_app_name(self):
        # Check name of app's configuration
        self.assertEqual(apps.get_app_config('flightseats').name, 'flightseats')

    def test_default_auto_field(self):
        # Check default auto field setting for the app's models
        self.assertEqual(apps.get_app_config('flightseats').default_auto_field, 'django.db.models.BigAutoField')

    def test_ready_method_deletes_existing_flights(self):
        # Create a Flight object
        Flight.objects.create(
            year=2023,
            month=12,
            day=31,
            airline='Lufthansa',
            flight_number=1954,
            origin_airport='HAM',
            dest_airport='ARN',
            departure='12:49'
        )
        # Check if there is 1 flight in the database
        self.assertEqual(Flight.objects.count(), 1)
        # Call ready method for flights app configs
        apps.get_app_config('flightseats').ready()
        # Check if the 4 loaded flights are back
        self.assertEqual(Flight.objects.count(), 4)


