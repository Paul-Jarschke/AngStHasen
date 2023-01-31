# The models.py defines the structure and tables of the database
# Defines our django models "Flight", "Book", and "Statistics"

from django.contrib import admin
from django.db import models
from django.http import HttpResponse


# Contains information about the flights
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


# Contains information about a booking, such as the seat choice, the person who made the reservation, and the booking time.
class Book(models.Model):
    seat_choice = models.CharField(max_length=30, default="none", unique=True)
    reserved_by = models.CharField(max_length=30, default="none")
    booking_time = models.CharField(max_length=30, default="none")

    def __str__(self):
        return self.seat_choice


# Contains information about all the seats on a flight. Information depending on ChartIn.txt
class Seats(models.Model):
    column_row_number = models.CharField(max_length=250, default="1")
    column_a = models.CharField(max_length=250, default="A")
    column_b = models.CharField(max_length=250, default="B")
    column_c = models.CharField(max_length=250, default="C")
    column_d = models.CharField(max_length=250, default="D")
    column_e = models.CharField(max_length=250, default="E")
    column_f = models.CharField(max_length=250, default="F")

    def __str__(self):
        return self.column_row_number


# Pseudo model for statistics page. No variables in table.
class Statistics(models.Model):
    class Meta:
        verbose_name_plural = "Statistics page"


# We create an EmptyModelAdmin for the Statistics page since this is just a pseudo model with no data. We need this to create an empty page where no data can be added and only html input can be shown.
# See templates/admin/flightseats/statistics/change_list.html for what is being displayeed in this empty model page.
class EmptyModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        from .statistics import all_seats, free_seats2, booked_seats, count_all, count_book, count_free, ratio_book, \
            ratio_free, \
            user_data, \
            count_users  # must be situated here, otherwise you receive an error that book model is not yet loaded.

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

    # the stat download crates an HttpResponse when clicked which writes a text file,
    # including all the data from the statistics-page
    def stat_download(self):
        from .statistics import all_seats, free_seats2, booked_seats, count_all, count_book, count_free, ratio_book, \
            ratio_free, \
            user_data, \
            count_users  # must be situated here, otherwise you receive an error that book model is not yet loaded.

        response = HttpResponse(content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename= booking_statistic.txt'

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

        lines.append(f'Count: {count_users}')

        response.writelines(lines)
        return response
