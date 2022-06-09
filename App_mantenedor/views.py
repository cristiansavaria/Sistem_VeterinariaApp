
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Insumo, Cliente, Paciente, Empleado, AppClienteContacto
from .forms import ClienteForm, InsumoForm, MedicoForm, PacienteForm, ContactoRForm
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.


def login(request):
    return render(request, 'registration/login.html')


@login_required()
def index(request):
    return render(request, 'index.html')


@login_required()
def clientes(request):
    cliente = Cliente.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(cliente, 7)
        cliente = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': cliente,
        'form': ClienteForm(),
        'paginator': paginator
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

        data["form"] = formulario

    return render(request, 'clientes.html', data)


@login_required()
def pacientes(request):
    pacientes = Paciente.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(pacientes, 7)
        pacientes = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': pacientes,
        'form': PacienteForm(),
        'paginator': paginator
    }
    if request.method == 'POST':
        formulario = PacienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

        data["form"] = formulario

    return render(request, 'pacientes.html', data)


@login_required()
def medico(request):
    medico = Empleado.objects.filter(tipo_empleado_idtip_emp=1)
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(medico, 7)
        medico = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': medico,
        'form': MedicoForm(),
        'paginator': paginator
    }
    if request.method == 'POST':
        formulario = MedicoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

        data["form"] = formulario

    return render(request, 'medico.html', data)


@login_required()
def insumos(request):
    insumos = Insumo.objects.all()
    page = request.GET.get('page', 1)
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


@login_required()
def reserva_horas(request):
    return render(request, 'reserva_horas.html')


@login_required()
def modificar_insumo(request, id_insumo):

    insumo = get_object_or_404(Insumo, id_insumo=id_insumo)
    data = {
        'form': InsumoForm(instance=insumo)
    }
    if request.method == 'POST':
        formulario = InsumoForm(
            data=request.POST, instance=insumo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="insumos")
        data["form"] = formulario

    return render(request, 'modificar_insumo.html', data)


@login_required()
def modificar_cliente(request, id_rut):
    cliente = get_object_or_404(Cliente, id_rut=id_rut)
    data = {
        'form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(
            data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="clientes")
        data["form"] = formulario

    return render(request, 'modificar_cliente.html', data)


@login_required()
def modificar_medico(request, id_emp):
    medico = get_object_or_404(Empleado, id_emp=id_emp)
    data = {
        'form': MedicoForm(instance=medico)
    }
    if request.method == 'POST':
        formulario = MedicoForm(
            data=request.POST, instance=medico, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="medico")
        data["form"] = formulario

    return render(request, 'modificar_medico.html', data)


@login_required()
def modificar_paciente(request, id_pac):
    paciente = get_object_or_404(Paciente, id_pac=id_pac)
    data = {
        'form': PacienteForm(instance=paciente)
    }
    if request.method == 'POST':
        formulario = PacienteForm(
            data=request.POST, instance=paciente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pacientes")
        data["form"] = formulario

    return render(request, 'modificar_paciente.html', data)


@login_required()
def contacto_recibido(request):
    contacto_re = AppClienteContacto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(contacto_re, 7)
        contacto_re = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': contacto_re,
        'form': ContactoRForm(),
        'paginator': paginator,

    }

    if request.method == 'POST':
        formulario = ContactoRForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        data["form"] = formulario

    return render(request, 'contacto_recibido.html', data)


def eliminar_insumo(request, id_insumo):
    insumoe = get_object_or_404(Insumo, id_insumo=id_insumo)
    insumoe.delete()
    return redirect(to="insumos")


def eliminar_empleado(request, id_emp):
    empleado = get_object_or_404(Empleado, id_emp=id_emp)
    empleado.delete()
    return redirect(to="medico")

def eliminar_cliente(request, id_rut):
    cliente = get_object_or_404(Cliente, id_rut=id_rut)
    cliente.delete()
    return redirect(to="clientes")

def eliminar_paciente(request, id_pac):
    paciente = get_object_or_404(Paciente, id_pac=id_pac)
    paciente.delete()
    return redirect(to="pacientes")