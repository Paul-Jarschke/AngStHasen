from django.shortcuts import render
from .models import Flight, Seats

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


def login(request):
    context = {
        'seats': Seats.objects.all()
    }
    return render(request, 'flightseats/login.html', context)


def help(request):
    return render(request, 'flightseats/help.html')

# Create your views here.
