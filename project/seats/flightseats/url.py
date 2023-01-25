from django.urls import path
from . import views
from users import views as views2

urlpatterns = [
    path('', views.home, name='flightseats-home'),
    path('flights/', views.flights, name='flights'),
    path('booking/', views.booking, name='booking'),
    path('help/', views.help, name='help'),
    path('register/', views2.register, name='register')
]
