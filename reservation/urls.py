from django.urls import path, include
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('booking/<int:barber_id>/<int:day_id>', booking, name="booking"),
    path('pre_reserva', pre_reserva, name='pre_reserva'),
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path('register', create_user, name="register"),
    path('schedules/<int:barber_id>', profile_page, name="schedules"),
    path('done/<int:cut_id>/<int:barber_id>', cut_done, name='cut_done'),
    path('cut_cancelled/<int:cut_id>/<int:barber_id>', cut_done, name='cut_cancelled'),
]