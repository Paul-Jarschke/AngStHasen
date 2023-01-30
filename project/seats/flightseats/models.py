from django.contrib import admin
from django.db import models
from django.http import HttpResponse
from django.contrib.auth import get_user_model


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


input = open("flightseats/data/chartIn.txt", 'r')
nrow = len(input.readlines())
seat_rows = list(map(str, range(nrow + 1)))[1:-1]  # gives string list of 1 up to number of rows
seat_letters = ['A', 'B', 'C', 'D', 'E', 'F']

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
free_seats2 = str(free_seats).replace("[", "").replace("]", "").replace("'", "")

# Number of booked seats:
count_book = len(booked_seats2)

# Number of free seats:
count_free = len(free_seats)

# Number of all seats:
count_all = len(all_seats_dummy)

# Ratios of booked/free seats:
ratio_book = str(round(((count_book / count_all) * 100), 2)) + "%"
ratio_free = str(round(((count_free / count_all) * 100), 2)) + "%"

# Data of users
User = get_user_model()
user_data = User.objects.values_list('username', 'first_name', 'last_name', 'email')
user_data = list(user_data)

# Number of users
count_users = len(user_data)


class EmptyModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        content = {
            'all_seats': all_seats,
            'free_seats': free_seats2,
            'booked_seats': booked_seats,
            'count_all': count_all,
            'count_book': count_book,
            'count_free': count_free,
            'ratio_book': ratio_book,
            'ratio_free': ratio_free,
            'user_data': user_data,
            'count_users': count_users
        }
        return super().changelist_view(request, extra_context=content)

    def stat_download(self):
        response = HttpResponse(content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename= flight_statistic.txt'

        lines = []
        lines.append(f"All possible seats:\n{all_seats}\n")
        lines.append(f"Count: {count_all}\n\n\n")

        lines.append(f"Free seats:\n{free_seats2}\n")
        lines.append(f"Count: {count_free}\n\n\n")

        lines.append(f"Booked seats:\n{booked_seats}\n")
        lines.append(f"Count: {count_book}\n\n\n")

        lines.append(f"Proportion of free seats:\n{ratio_free}\n\n\n")

        lines.append(f"Proportion of booked seats:\n{ratio_book}\n\n\n")

        lines.append(f"User list:\n")
        for user in user_data:
            lines.append(f'Username: {user[0]}\n')
            lines.append(f'Full name: {user[1]} {user[2]}\n')
            lines.append(f'E-Mail: {user[3]}\n')
            lines.append(f'\n')

        response.writelines(lines)
        return response
