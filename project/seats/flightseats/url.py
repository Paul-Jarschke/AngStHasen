from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'flightseats-home'),
    path('booking/<int:flightnumber>',views.booking, name = 'booking'),
    path('login/', views.login, name = 'login')
]