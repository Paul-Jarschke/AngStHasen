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


class book(models.Model):
    airline = models.CharField(max_length=250, default="Airline")  # put this as foreign key
    # load different datasets dependend on airline foreign key from seats


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
        return self.column_i


class User(models.Model):
    name = models.CharField(max_length=250, default="empty")
    user_name = models.CharField(max_length=250, default="empty")
    password = models.CharField(max_length=250, default="empty")

    def __str__(self):
        return self.airline


class Seats2(models.Model):
    rows = seat_data
