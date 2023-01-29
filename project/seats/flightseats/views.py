# This file defines the general functionality of the website itself. Combines python objects with html files.
from django.shortcuts import render
from .models import Flight, Seats, Book, UserBooking
import numpy as np
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth import get_user_model


def home(request):
    if request.user.is_authenticated:  # indicator variable that is needed for showing different outputs.
        auth_ind = "True"
    else:
        auth_ind = "False"

    current_user = request.user  # needed for showing username on startpage

    context = {
        'auth_ind': auth_ind,
        'current_user': current_user
    }  # pass these objects to html // this is the same for every def XYZ()
    return render(request, 'flightseats/home.html', context)


def flights(request):
    context = {
        'flights_bookable': Flight.objects.all()[0:1],  # first object is clickable/bookable
        'flights_rest': Flight.objects.all()[1:],  # bookable
        'current_user': request.user  # needed for black header on every page
    }
    return render(request, 'flightseats/flights.html', context)


def booking(request):
    # Get list of booked seats from DB
    booked_seats = list(map(str, Book.objects.all()))

    # Create chartIn_reservation.txt
    # take booked_seats from DB und show them as X based on the template chartIn.txt
    row_numbers = [seat[:-1] for seat in booked_seats]
    seat_letters = [seat[-1:] for seat in booked_seats]

    # Read lines from input file
    with open("flightseats/data/chartIn.txt", 'r') as input_file:
        input_lines = input_file.readlines()

    # Replace booked seats with 'X'
    for i, row_number in enumerate(row_numbers):
        if int(row_number) <= len(input_lines):
            input_lines[int(row_number) - 1] = input_lines[int(row_number) - 1].replace(seat_letters[i], "X")

    # Write updated input lines to output file
    with open("flightseats/data/chartIn_reservations.txt", 'w') as output_file:
        output_file.writelines(input_lines)

    # Load seat data from output file
    seat_data = np.loadtxt("flightseats/data/chartIn_reservations.txt", dtype='str')
    row_count = len(seat_data)
    row_list = str(list(map(str, range(row_count + 1)))[1:])

    # Save new reservations from POST to book in DB (if user is logged in only!)
    if request.user.is_authenticated:
        auth_ind = "True"
        if request.method == 'POST':
            seat_choice_row = request.POST.get('seat_choice_row')
            seat_letter = request.POST.get('seatletter')
            if (seat_choice_row in row_list) and (seat_letter in ['A', 'B', 'C', 'D', 'E', 'F']) and (
                    seat_choice_row + seat_letter) not in booked_seats:
                book = Book(seat_choice=seat_choice_row + seat_letter)
                book.save()
                reservations = UserBooking(seat_choice=seat_choice_row + seat_letter, reserved_by=request.user)
                reservations.save()
    else:
        auth_ind = "False"

    # Delete previous seat entries and create new ones
    Seats.objects.all().delete()
    for i in range(len(seat_data)):
        Seats.objects.create(
            column_row_number=seat_data[i][0],
            column_a=seat_data[i][1],
            column_b=seat_data[i][2],
            column_c=seat_data[i][3],
            column_d=seat_data[i][4],
            column_e=seat_data[i][5],
            column_f=seat_data[i][6]
        )

    context = {
        'seats': Seats.objects.all(),
        'rowcount': row_count,
        'rowlist': row_list,
        'bookedseats': booked_seats,
        'auth_ind': auth_ind,
        'current_user': request.user
    }
    return render(request, 'flightseats/booking.html', context)


def help(request):
    context = {
        'current_user': request.user
    }
    return render(request, 'flightseats/help.html', context)


def statistics_text(request):
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

    # Number of booked_seats:
    count_book = len(booked_seats)

    # Number of free seats:
    count_free = len(free_seats)

    # Number of all seats:
    count_all = len(all_seats)

    # Ratios of booked/free seats:
    ratio_book = str(round(((count_book / count_all) * 100), 2)) + "%"
    ratio_free = str(round(((count_free / count_all) * 100), 2)) + "%"

    User = get_user_model()
    objects = User.objects.values_list('username', 'first_name', 'last_name', 'email')
    users = list(objects)

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename= flight_statistic.txt'

    lines = []

    for x in users:
        for y in x:
            lines.append(f'{y}\n')
        lines.append(f'\n')

    lines.append(f'{ratio_free}\n')
    lines.append(f'{ratio_book}\n')
    lines.append(f'{free_seats}\n')
    lines.append(f'{booked_seats}\n')

    response.writelines(lines)
    return response
