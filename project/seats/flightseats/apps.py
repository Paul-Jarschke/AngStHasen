from django.apps import AppConfig


class FlightseatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flightseats'

    def ready(self):
        from .models import Flight
        # This file checks existence of custom flights and users on server startup and creates the data if necessary
        # Create custom flights for our DB
        # if 1 == 1:  # guarantee that we have at least four custom flights in our DB
        #   Flight.objects.all().delete()

        if len(Flight.objects.all()) < 4:  # guarantee that we have at least four custom flights in our DB
            Flight.objects.all().delete()

            # From Hamburg to Arlanda/Stockholm
            Flight.objects.create(
                year=2023,
                month=10,
                day=22,
                airline="Lufthansa",
                flight_number=1954,
                origin_airport="HAM",
                dest_airport="ARN",
                departure="12:49"
            )

            # From Berlin to New York
            Flight.objects.create(
                year=2023,
                month=3,
                day=1,
                airline="Lufthansa",
                flight_number=982,
                origin_airport="BER",
                dest_airport="JFK",
                departure="09:10"
            )

            # From Frankfurt to Dubai
            Flight.objects.create(
                year=2023,
                month=8,
                day=12,
                airline="Emirates",
                flight_number=1044,
                origin_airport="FRA",
                dest_airport="DXB",
                departure="20:22"
            )

            # From Nuremberg to Palma de Mallorca
            Flight.objects.create(
                year=2023,
                month=4,
                day=24,
                airline="RYANAIR",
                flight_number=121,
                origin_airport="NUE",
                dest_airport="PMI",
                departure="14:12"
            )

# class UsersConfig(AppConfig):
#    default_auto_field = 'django.db.models.BigAutoField'
#    name = 'users'
#
#    def ready(self):
#        from .models import User
#
#        from django.contrib.auth.models import User
#        User.objects.create_user(user_name='Tim',
#                                 email='tim@python.com',
#                                 password='apfelringe')
#
