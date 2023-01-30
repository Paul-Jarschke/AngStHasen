from django.urls import path
from . import views
from users import views as views2
from . import models

urlpatterns = [
    path('', views.home, name='flightseats-home'),
    path('flights/', views.flights, name='flights'),
    path('booking/', views.booking, name='booking'),
    path('help/', views.help, name='help'),
    path('register/', views2.register, name='register'),
    path('stats_text/', models.EmptyModelAdmin.stat_download, name='stats_txt')
]
