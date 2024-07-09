from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from . models import *


def home(request):
    reservas = Reserva.objects.all()

    context = {
        'reservas': reservas,
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
def reserva(request, barber_id, day_id):
    day = ServicoDia.objects.get(id=day_id)
    barber = barber_id

    available_time_slots = get_time_slots(day, barber)

    if request.method == 'POST':
        time_slot_id = request.POST.get('time_slot')
        user = request.user
        time_slot = ServicoHorario.objects.get(id=time_slot_id)

        Reserva.objects.create(day=day, time=time_slot, user=user, barber=barber)

        return redirect('home')
    
    context = {
        'day': day,
        'barber': barber,
        'available_time_slots': available_time_slots,
    }

    return render(request, 'reserva.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    
    return render(request, 'login.html')


def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validar Dados
        if not username or not email or not password:
            messages.add_message(request, messages.ERROR, 'Preencha todos os campos!')
            return render(request, 'register.html')
        
        # Validar se Username já existe
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, 'Username já existe')
            return render(request, 'register.html')
        
        # Validar se Email já existe
        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'Email já existe')
            return render(request, 'register.html')
        
        # Criar User
        user = User.objects.create(
            username = username,
            first_name = fname,
            last_name = lname,
            email = email,
            password = make_password(password)
        )

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
    return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def pre_reserva(request):
    barbeiro = User.objects.filter()
    days = ServicoDia.objects.all()

    context = {
        'days': days,
    }
    return render(request, 'pre_reserva.html', context)