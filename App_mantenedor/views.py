from django.shortcuts import render
from .models import Insumo, Cliente, Paciente
from .forms import InsumoForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
def clientes(request):
    cliente = Cliente.objects.all()
    data = {
        'cliente' : cliente
    }
    return render(request, 'clientes.html', data)

def pacientes(request):
    pacientes = Paciente.objects.all()
    data = {
        'pacientes' : pacientes
    }

    return render(request, 'pacientes.html', data)
def medico(request):
    return render(request, 'medico.html')


def insumos(request):
    
    
    insumos = Insumo.objects.all()
    data = {
        'insumos': insumos,
        'form': InsumoForm()
    }
    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            
            
            
        data["form"] = formulario


    return render(request, 'insumos.html', data)





def reserva_horas(request):
    return render(request, 'reserva_horas.html')


