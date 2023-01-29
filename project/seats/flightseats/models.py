from django.db import models
from django.contrib import admin
from django.contrib.admin.actions import delete_selected
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


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
    column_row_number = models.CharField(max_length=250, default="1")
    column_a = models.CharField(max_length=250, default="A")
    column_b = models.CharField(max_length=250, default="B")
    column_c = models.CharField(max_length=250, default="C")
    column_d = models.CharField(max_length=250, default="D")
    column_e = models.CharField(max_length=250, default="E")
    column_f = models.CharField(max_length=250, default="F")

    def __str__(self):
        return self.column_row_number


class User(models.Model):
    name = models.CharField(max_length=250, default="empty")
    user_name = models.CharField(max_length=250, default="empty", unique=True)
    password = models.CharField(max_length=250, default="empty")

    def __str__(self):
        return self.name


class UserBooking(models.Model):
    seat_choice = models.CharField(max_length=30, default="none", unique=True)
    reserved_by = models.CharField(max_length=30, default="none")

    def __str__(self):
        return self.reserved_by


class Statistics(models.Model):
    class Meta:
        verbose_name_plural = "Statistics page"


class EmptyModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # All seats list:
        input = open("flightseats/data/chartIn.txt", 'r')
        nrow = len(input.readlines())
        seat_rows = list(map(str, range(nrow + 1)))[1:]  # gives string list of 1 up to number of rows
        seat_letters = ['A', 'B', 'C', 'D', 'F']

        all_seats_dummy = []
        for r in seat_rows:
            for l in seat_letters:
                all_seats_dummy.append(r + l)

        all_seats = str(all_seats_dummy).replace("[", "").replace("]", "").replace("'", "")

        # Booked seats list:
        booked_seats = str(list(map(str, Book.objects.all()))).replace("[", "").replace("]", "").replace("'", "")

        # Reserved seats list:
        booked_seats2 = list(map(str, Book.objects.all()))
        free_seats = [x for x in all_seats_dummy if x not in booked_seats2]
        free_seats = str(free_seats).replace("[", "").replace("]", "").replace("'", "")

        # Number of bookedseats:
        count_book = len(booked_seats)

        # Number of free seats:
        count_free = len(free_seats)

        # Number of all seats:
        count_all = len(all_seats)

        # Ratios of booked/free seats:
        ratio_book = str(round(((count_book / count_all) * 100), 2)) + "%"
        ratio_free = str(round(((count_free / count_all) * 100), 2)) + "%"

        # Number of users
        # user_count = len(User.objects.all())

        # Data of users
        User = get_user_model()
        email = User.objects.values_list('username', 'first_name', 'last_name', 'email')
        users = list(email)

        content = {
            'all_seats': all_seats,
            'free_seats': free_seats,
            'booked_seats': booked_seats,
            'ratio_book': ratio_book,
            'ratio_free': ratio_free,
            'users': users

        }
        return super().changelist_view(request, extra_context=content)
