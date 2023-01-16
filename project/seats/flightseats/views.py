from django.shortcuts import render
from .models import Flight, Seats
import numpy as np

flights = [
    {
        'year': '2015',
        'month': '1',
        'day': '1',
        'airline': 'US',
        'flight_number': '112',
        'origin_airport': 'SEA',
        'dest_airport': 'ANC',
        'departure': '23:00'

    },
    {
        'year': '2015',
        'month': '1',
        'day': '1',
        'airline': 'US',
        'flight_number': '112',
        'origin_airport': 'SEA',
        'dest_airport': 'ANC',
        'departure': '23:00'
    }
]


def home(request):
    context = {
        'flights': Flight.objects.all()
    }
    return render(request, 'flightseats/home.html', context)


def booking(request, flightnumber):
    context = {'flightnumber': flightnumber}
    return render(request, 'flightseats/booking.html', context)


seat_data = np.loadtxt("flightseats/data/chartIn.txt", dtype='str')
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


def login(request):
    context = {
        'seats': Seats.objects.all()
    }
    return render(request, 'flightseats/login.html', context)


def help(request):
    return render(request, 'flightseats/help.html')

# Create your views here.
