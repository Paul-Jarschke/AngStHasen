from django.test import TestCase
from django.urls import reverse, resolve
from ..views import home, flights, booking, help



class TestUrls(TestCase):

    def test_home_url_resolve(self):
        url = reverse('flightseats-home')
        self.assertEqual(resolve(url).func, home)

    def test_flights_url_resolve(self):
        url = reverse('flights')
        self.assertEqual(resolve(url).func, flights)

    def test_booking_url_resolve(self):
        url = reverse('booking')
        self.assertEqual(resolve(url).func, booking)

    def test_help_url_resolve(self):
        url = reverse('help')
        self.assertEqual(resolve(url).func, help)

    #def test_register_url_resolve(self):
        #url = reverse('flightseats-home')
        #self.assertEqual(resolve(url).func, register)

    # register is missing but where is it written ?
        #written in users.


    #path('', views.home, name='flightseats-home'),
    #path('flights/', views.flights, name='flights'),
    #path('booking/', views.booking, name='booking'),
    #path('help/', views.help, name='help'),
    #path('register/', views2.register, name='register')
