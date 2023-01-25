# This file defines the general functionality of the website itself. Combines python objects with html files.


from django.shortcuts import render
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
    bookedseats = list(map(str, Book.objects.all()))  # returns list of booked from DB

    # Create chartIn_reservation.txt which takes bookedseats from DB und shows them as X based on the template chartIn.txt:
    brow = []
    bletter = []
    for element in bookedseats:  # separate letter and number to show X on webpage
        brow.append(element[:-1])
        bletter.append(element[-1:])

    input = open("flightseats/data/chartIn.txt", 'r')
    ilines = input.readlines()
    brow = [int(x) for x in brow]

    newlines = ilines

    for pos in range(len(ilines)):
        rownumber = pos + 1

        if rownumber in brow:
            for nr, element in enumerate(brow):
                if element == rownumber:
                    newlines[pos] = newlines[pos].replace(bletter[nr], "X")  # if reserved, then 'X'
        else:
            newlines[pos] = ilines[pos]  # if not take value from chartIn.txt template

    output = open("flightseats/data/chartIn_reservations.txt", 'r')

    output.writelines(newlines)
    output.close()

    global seat_data
    seat_data = np.loadtxt("flightseats/data/chartIn_reservations.txt", dtype='str')
    rowcount = len(seat_data)
    rowlist = str(list(map(str, range(rowcount + 1)))[1:])

    if request.user.is_authenticated:  # save new reservations from POST to book in DB (if user is logged in only!)
        auth_ind = "True"
        if request.method == 'POST':
            if (request.POST.get('seat_choice_row') in list(map(str, list(range(rowcount + 1))[1:])) and
                (request.POST.get('seatletter') in ['A', 'B', 'C', 'D', 'F']) and
                    (request.POST.get('seat_choice_row') + request.POST.get('seatletter'))) not in bookedseats:
                book = Book()
                reservations = UserBooking()
                book.seat_choice = request.POST.get('seat_choice_row') + request.POST.get('seatletter')
                reservations.seat_choice = request.POST.get('seat_choice_row') + request.POST.get('seatletter')
                reservations.reserved_by = request.user
                reservations.save()
                book.save()
    else:
        auth_ind = "False"

    context = {
        'seats': Seats.objects.all(),
        'rowcount': rowcount,
        'rowlist': rowlist,
        'bookedseats': bookedseats,
        'auth_ind': auth_ind,
        'current_user': request.user
    }
    entries = Seats.objects.all()
    entries.delete()

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
    return render(request, 'flightseats/booking.html', context)


def help(request):
    context = {
        'current_user': request.user
    }
    return render(request, 'flightseats/help.html', context)
