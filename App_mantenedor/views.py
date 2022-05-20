from django.shortcuts import render
from .models import Insumo

# Create your views here.
def index(request):
    return render(request, 'index.html')
def clientes(request):
    return render(request, 'clientes.html')
def pacientes(request):
    return render(request, 'pacientes.html')
def insumos(request):
    insumos = Insumo.objects.all()
    data = {
        'insumos': insumos
    }
    return render(request, 'insumos.html', data)
def reserva_horas(request):
    return render(request, 'reserva_horas.html')
