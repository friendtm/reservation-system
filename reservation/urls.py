from django.urls import path, include
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('reserva/<int:barber_id>/<int:day_id>', reserva, name="reserva"),
    path('pre_reserva', pre_reserva, name='pre_reserva'),
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path('register', create_user, name="register"),
]