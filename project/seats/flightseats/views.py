from django.shortcuts import render
from .models import Flight, Seats, Book
import numpy as np


def home(request):
    context = {
        'flights': Flight.objects.all()
    }
    return render(request, 'flightseats/home.html', context)


def booking(request, flightnumber):
    context = {'flightnumber': flightnumber}
    return render(request, 'flightseats/booking.html', context)


def login(request):
    if request.method == 'POST':
        if request.POST.get('seat_choice'):
            book = Book()
            book.seat_choice = request.POST.get('seat_choice')
            book.save()

    context = {
        'seats': Seats.objects.all()
    }
    global seat_data
    seat_data = np.loadtxt("flightseats/data/chartIn.txt", dtype='str')
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
    return render(request, 'flightseats/login.html', context)


def help(request):
    return render(request, 'flightseats/help.html')
