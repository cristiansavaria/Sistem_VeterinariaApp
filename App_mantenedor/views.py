from sqlite3 import DatabaseError
from django.shortcuts import render, redirect, get_object_or_404
from .models import Insumo, Cliente, Paciente, Empleado, TipoEmpleado
from .forms import InsumoForm, PacienteForm
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
        'pacientes' : pacientes,
        'form': PacienteForm()
    }
    if request.method == 'POST':
        formulario = PacienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            
            
            
        data["form"] = formulario

    return render(request, 'pacientes.html', data)

def medico(request):

    medico = Empleado.objects.filter(tipo_empleado_idtip_emp = 1)
    data = {
        'medico' : medico,
    }
       
    return render(request, 'medico.html', data)


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



def modificar_insumo(request, id_insumo):
    
    insumo = get_object_or_404(Insumo, id_insumo=id_insumo)
    data = {
        'form': InsumoForm(instance=insumo)
    }
    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST, instance=insumo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="insumos")
        data["form"] = formulario


    return render(request, 'modificar_insumo.html', data)
