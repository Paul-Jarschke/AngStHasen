# This file defines the general functionality of the website itself. Combines python objects with html files.
from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Flight, Seats, Book, UserBooking
import numpy as np


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
            if (seat_choice_row in row_list) and (seat_letter in ['A', 'B', 'C', 'D', 'E', 'F']) and (seat_choice_row + seat_letter) not in booked_seats:
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
            column_a=seat_data[i][0],
            column_b=seat_data[i][1],
            column_c=seat_data[i][2],
            column_d=seat_data[i][3],
            column_e=seat_data[i][4],
            column_f=seat_data[i][5],
            column_g=seat_data[i][6]
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
    return TemplateResponse(request, 'flightseats/help.html', context)
