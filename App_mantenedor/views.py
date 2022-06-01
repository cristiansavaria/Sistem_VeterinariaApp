from sqlite3 import DatabaseError
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Insumo, Cliente, Paciente, Empleado, TipoEmpleado
from .forms import ClienteForm, InsumoForm, MedicoForm, PacienteForm
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.



def index(request):
    return render(request, 'index.html')


def clientes(request):
    cliente = Cliente.objects.all()
    data = {
        'cliente' : cliente,
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            
        data["form"] = formulario

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
        'form': MedicoForm()
    }
    if request.method == 'POST':
        formulario = MedicoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            
        data["form"] = formulario
       
    return render(request, 'medico.html', data)


def insumos(request):
    
    
    insumos = Insumo.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(insumos, 7)
        insumos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': insumos,
        'form': InsumoForm(),
        'paginator': paginator
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

def modificar_cliente(request, id_rut):
    cliente = get_object_or_404(Cliente, id_rut=id_rut)
    data = {
        'form':ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="clientes")
        data["form"] = formulario


    return render(request, 'modificar_cliente.html', data)

def modificar_medico(request, id_emp):
    medico = get_object_or_404(Empleado, id_emp=id_emp)
    data = {
        'form':MedicoForm(instance=medico)
    }
    if request.method == 'POST':
        formulario = MedicoForm(data=request.POST, instance=medico, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="medico")
        data["form"] = formulario


    return render(request, 'modificar_medico.html', data)

def modificar_paciente(request, id_pac):
    paciente = get_object_or_404(Paciente, id_pac=id_pac)
    data = {
        'form': PacienteForm(instance=paciente)
    }
    if request.method == 'POST':
        formulario = PacienteForm(data=request.POST, instance=paciente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pacientes")
        data["form"] = formulario


    return render(request, 'modificar_paciente.html', data)






def login_admin(request):
    return render(request, 'login_admin.html')