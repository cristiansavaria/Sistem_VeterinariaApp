from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def clientes(request):
    return render(request, 'clientes.html')
def pacientes(request):
    return render(request, 'pacientes.html')
def insumos(request):
    return render(request, 'insumos.html')
def reserva_horas(request):
    return render(request, 'reserva_horas.html')
