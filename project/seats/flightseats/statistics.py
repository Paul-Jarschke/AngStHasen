from .models import Book
from django.contrib.auth import get_user_model

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
