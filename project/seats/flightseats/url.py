from django.urls import path
from . import views
from users import views as views2

urlpatterns = [
    path('', views.home, name='flightseats-home'),
    path('booking/<int:flightnumber>', views.booking, name='booking'),
    path('login/', views.login, name='login'),
    path('help/', views.help, name='help'),
    path('register/', views2.register, name='register')
]
