from typing import Any
from django.db import models
from django.contrib.auth.models import User

class ServicoDia(models.Model):
    day = models.CharField(max_length=7)

    def __str__(self):
        return self.day
    

class ServicoHorario(models.Model):
    time = models.CharField(max_length=9)

    def __str__(self):
        return self.time


class Reserva(models.Model):
    day = models.ForeignKey(ServicoDia, on_delete=models.CASCADE)
    time = models.ForeignKey(ServicoHorario, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barber = models.IntegerField()
    is_done = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return self.time.time
    

def get_time_slots(day, barber):
    # Get all time slots
    all_time_slots = ServicoHorario.objects.all()
    
    # Get booked time slots for the specific day and barber
    booked_time_slots = Reserva.objects.filter(day=day, barber=barber).values_list('time', flat=True)
    
    # Get available time slots by excluding booked time slots
    available_time_slots = all_time_slots.exclude(id__in=booked_time_slots)
    
    return available_time_slots