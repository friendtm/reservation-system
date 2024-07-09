from django.contrib import admin
from . models import *


@admin.register(ServicoDia)
class ServicoDiaAdmin(admin.ModelAdmin):
    list_display = ('day',)
    search_fields = ('day',)


@admin.register(ServicoHorario)
class ServicoHorarioAdmin(admin.ModelAdmin):
    list_display = ('time',)
    search_fields = ('time',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'time', 'barber', 'is_done', 'is_canceled')
    list_filter = ('is_done', 'is_canceled', 'day', 'time', 'barber')
    search_fields = ('user__username', 'day__day', 'time__time', 'barber')