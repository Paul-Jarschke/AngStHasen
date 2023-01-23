from django.db import models
import numpy as np

seat_data = np.loadtxt("flightseats/data/chartIn.txt", dtype='str')


class Flight(models.Model):
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    airline = models.CharField(max_length=250, default="Airline")
    flight_number = models.IntegerField(default=0)
    origin_airport = models.CharField(max_length=250, default="Airport")
    dest_airport = models.CharField(max_length=250, default="destination")
    departure = models.CharField(max_length=250, default="Time")

    def __str__(self):
        return self.airline


class Book(models.Model):
    seat_choice = models.CharField(max_length=30, default="none", unique=True)

    def __str__(self):
        return self.seat_choice


class Seats(models.Model):
    # booked = models.BooleanField()
    # update datasets
    column_a = models.CharField(max_length=250, default="A")
    column_b = models.CharField(max_length=250, default="A")
    column_c = models.CharField(max_length=250, default="A")
    column_d = models.CharField(max_length=250, default="A")
    column_e = models.CharField(max_length=250, default="A")
    column_f = models.CharField(max_length=250, default="A")
    column_g = models.CharField(max_length=250, default="A")

    def __str__(self):
        return self.column_a


class User(models.Model):
    name = models.CharField(max_length=250, default="empty", unique=True)
    # shouldn't unique = False for name ? 2 different Pauls cant do booking otherwise!!!
    user_name = models.CharField(max_length=250, default="empty", unique=True)
    password = models.CharField(max_length=250, default="empty")

    def __str__(self):
        return self.name


class Seats2(models.Model):
    rows = models.CharField(max_length=250, default="A")
