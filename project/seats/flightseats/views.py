from django.shortcuts import render
from .models import Flight, Seats, Book
import numpy as np


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


def booking(request, flightnumber):
    global seat_data
    seat_data = np.loadtxt("flightseats/data/chartIn.txt", dtype='str')
    rowcount = len(seat_data)
    rowlist = str(list(map(str, range(rowcount + 1)))[1:])
    bookedseats = list(map(str, Book.objects.all()))

    if request.method == 'POST':
        if (request.POST.get('seat_choice_row') in list(map(str, list(range(rowcount + 1))[1:])) and \
            (request.POST.get('seatletter') in ['A', 'B', 'C', 'D', 'F']) and \
            (request.POST.get('seat_choice_row') + request.POST.get('seatletter'))) not in bookedseats:
            book = Book()
            book.seat_choice = request.POST.get('seat_choice_row') + request.POST.get('seatletter')
            book.save()

        try:
            with open("flightseats/data/chartIn.txt",
                      'r+') as file:
                lines = file.readlines()
                bookedline = lines[int(request.POST.get('seat_choice_row')) - 1]
                bookedline = bookedline.replace(request.POST.get('seatletter'), "X")

                lines[int(request.POST.get('seat_choice_row')) - 1] = bookedline

                file.seek(0)
                file.truncate()
                for line in lines:
                    file.write(line)
                file.close
        except:
            pass

    context = {
        'seats': Seats.objects.all(),
        'rowcount': rowcount,
        'rowlist': rowlist,
        'bookedseats': bookedseats,
        'flightnumber': flightnumber
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
