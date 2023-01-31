# This file includes django apps for our models.
# It is especially checking the existence of custom flights and users on server startup and creates the data if necessary.

from django.apps import AppConfig


class FlightseatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flightseats'
