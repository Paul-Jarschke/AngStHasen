from django.shortcuts import render
from .models import Flight, Seats, Book
import numpy as np
from django.contrib.admin.models import LogEntry


def home(request):
    context = {
    }
    return render(request, 'flightseats/home.html', context)


def flights(request):
    context = {
        'flights_bookable': Flight.objects.all()[0:1],
        'flights_rest': Flight.objects.all()[1:]
    }
    return render(request, 'flightseats/flights.html', context)


def booking(request):
    bookedseats = list(map(str, Book.objects.all()))

    brow = []
    bletter = []
    for element in bookedseats:
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
                    newlines[pos] = newlines[pos].replace(bletter[nr], "X")
        else:
            newlines[pos] = ilines[pos]

    output = open("flightseats/data/chartIn_reservations.txt", 'r+')

    output.writelines(newlines)
    output.close

    global seat_data
    seat_data = np.loadtxt("flightseats/data/chartIn_reservations.txt", dtype='str')
    rowcount = len(seat_data)
    rowlist = str(list(map(str, range(rowcount + 1)))[1:])

    if request.user.is_authenticated:
        auth_ind = "True"
        if request.method == 'POST':
            if (request.POST.get('seat_choice_row') in list(map(str, list(range(rowcount + 1))[1:])) and \
                (request.POST.get('seatletter') in ['A', 'B', 'C', 'D', 'F']) and \
                (request.POST.get('seat_choice_row') + request.POST.get('seatletter'))) not in bookedseats:
                book = Book()
                book.seat_choice = request.POST.get('seat_choice_row') + request.POST.get('seatletter')
                book.save()


    else:
        auth_ind = "False"

    context = {
        'seats': Seats.objects.all(),
        'rowcount': rowcount,
        'rowlist': rowlist,
        'bookedseats': bookedseats,
        'auth_ind': auth_ind
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
    return render(request, 'flightseats/help.html')
