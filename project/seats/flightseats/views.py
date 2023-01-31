# This file defines the general functionality of the website itself. Combines python objects with html files.
from django.shortcuts import render
from .models import Flight, Seats, Book
import numpy as np
from datetime import datetime as dt


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
    # Create custom flights for our DB
    # if condition is True:  # guarantee that we have at least four custom flights in our DB
    if len(Flight.objects.all()) < 4:  # guarantee that we have at least four custom flights in our DB
        Flight.objects.all().delete()

        # From Hamburg to Arlanda/Stockholm
        Flight.objects.create(
            year=2023,
            month=10,
            day=22,
            airline='Lufthansa',
            flight_number=1954,
            origin_airport='HAM',
            dest_airport='ARN',
            departure='12:49'
        )

        # From Berlin to New York
        Flight.objects.create(
            year=2023,
            month=3,
            day=1,
            airline='Lufthansa',
            flight_number=982,
            origin_airport='BER',
            dest_airport='JFK',
            departure='09:10'
        )

        # From Frankfurt to Dubai
        Flight.objects.create(
            year=2023,
            month=8,
            day=12,
            airline='Emirates',
            flight_number=1044,
            origin_airport='FRA',
            dest_airport='DXB',
            departure='20:22'
        )

        # From Nuremberg to Palma de Mallorca
        Flight.objects.create(
            year=2023,
            month=4,
            day=24,
            airline='RYANAIR',
            flight_number=121,
            origin_airport='NUE',
            dest_airport='PMI',
            departure='14:12'
        )

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
                book = Book(seat_choice=seat_choice_row + seat_letter, reserved_by=request.user,
                            booking_time=dt.today().strftime('%Y-%m-%d %H:%M:%S'))
                book.save()
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
