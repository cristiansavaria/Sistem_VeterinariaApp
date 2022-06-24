
from django.http import Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Insumo, Cliente, Paciente, Empleado, AppClienteContacto, Reserva, HrsDispo, ProcedPacien
from .forms import ClienteForm, InsumoForm, ProcedimientoPForm, MedicoForm, PacienteForm,\
 ContactoRForm, ReservaForm, HrsDispoForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages


# Create your views here.


def login(request):
    return render(request, 'registration/login.html')


@login_required()
def index(request):
    return render(request, 'index.html')


@login_required()
def clientes(request):
    busqueda = request.GET.get("buscar")
    print(busqueda)
    cliente = Cliente.objects.all()

    if busqueda:
        cliente = Cliente.objects.filter(
            Q(id_rut__icontains = busqueda) |
            Q(nom_cli__icontains = busqueda) |
            Q(ap_cli__icontains = busqueda) 
    ).distinct()
    

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
            messages.success(request, "Cliente Agregado Correctamente")
            return redirect(to="clientes")

        data["form"] = formulario

  
    return render(request, 'clientes.html',data)


@login_required()
def pacientes(request):
    busqueda = request.GET.get("buscar")
    pacientes = Paciente.objects.all()
    
    
    
    if busqueda:
        pacientes = Paciente.objects.filter(
            Q(nom_pac__icontains = busqueda) |
            Q(raza__icontains = busqueda)|
            Q(cliente_id_rut = busqueda)

    ).distinct()
    
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
            messages.success(request, "Paciente Agregado Correctamente")
            return redirect(to="pacientes")
        data["form"] = formulario

    return render(request, 'pacientes.html', data)


@login_required()
def medico(request):
    busqueda = request.GET.get("buscar")
    medico = Empleado.objects.filter(tipo_empleado_idtip_emp=1)

    if busqueda:
        medico = Empleado.objects.filter(
            Q(id_emp__icontains = busqueda)|
            Q(nom_emp__icontains = busqueda) |
            Q(ap_emp__icontains= busqueda)

    ).distinct()
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
            messages.success(request, "Medico Agregado Correctamente")
            return redirect(to="medico")
        data["form"] = formulario

    return render(request, 'medico.html', data)


@login_required()
def insumos(request):
    busqueda = request.GET.get("buscar")
    insumos = Insumo.objects.all()

    
    if busqueda:
        insumos = Insumo.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(inventario__icontains = busqueda) 
    ).distinct()

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
            messages.success(request, "Insumo Agregado Correctamente")
            return redirect(to="insumos")
        data["form"] = formulario

    return render(request, 'insumos.html', data)


@login_required()
def reserva_horas(request ):
    reserva = Reserva.objects.all()
    data = {
        'reserva': reserva,
        'form': ReservaForm()
    }
    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Reserva Exitosa!")
            return redirect(to="reserva_horas")
        data["form"] = formulario

    return render(request, 'reserva_horas.html',data)


@login_required()
def horas_disponibles(request):
    horasdisponibles = HrsDispo.objects.all()

    data = {
        'horas_disponibles': horasdisponibles,
        'form': HrsDispoForm()
    }
    if request.method == 'POST':
        formulario = HrsDispoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="horas_disponibles")
        data["form"] = formulario

    return render(request, 'horas_disponibles.html', data)

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
            messages.success(request, "Insumo Modificado Correctamente")
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
            messages.success(request, "Cliente Modificado Correctamente")
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
            messages.success(request, "Medico Modificado Correctamente")
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
            messages.success(request, "Paciente Modificado Correctamente")
            return redirect(to="pacientes")
        data["form"] = formulario

    return render(request, 'modificar_paciente.html', data)

@login_required()
def modificar_reserva(request, id_res):
    reserva = get_object_or_404(Reserva, id_res=id_res)
    data = {
        'form': ReservaForm(instance=reserva)
    }
    if request.method == 'POST':
        formulario = ReservaForm(
            data=request.POST, instance=reserva, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Reserva Modificada Correctamente")
            return redirect(to="reserva_horas")
        data["form"] = formulario

    return render(request, 'modificar_reserva.html', data)

@login_required()
def modificar_hdisponible(request, idhrs_dispo):
    horasdisponibles = get_object_or_404(HrsDispo, idhrs_dispo=idhrs_dispo)
    data = {
        'form': HrsDispoForm(instance=horasdisponibles)
    }
    if request.method == 'POST':
        formulario = HrsDispoForm(
            data=request.POST, instance=horasdisponibles, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="horas_disponibles")
        data["form"] = formulario

    return render(request, 'modificar_hdisponible.html', data)

@login_required()
def modificar_proced(request, idpro_pac):
    proced = get_object_or_404(ProcedPacien, idpro_pac=idpro_pac)
    data = {
        'form': ProcedimientoPForm(instance=proced)
    }
    if request.method == 'POST':
        formulario = ProcedimientoPForm(
            data=request.POST, instance=proced, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Procedimiento Editado Correctamente")
            return redirect(to="procedimientos")
        data["form"] = formulario

    return render(request, 'modificar_proced.html', data)

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
    messages.success(request, 'Insumo Eliminado Correctamente')
    return redirect(to="insumos")


def eliminar_empleado(request, id_emp):
    empleado = get_object_or_404(Empleado, id_emp=id_emp)
    empleado.delete()
    messages.success(request, 'Empleado Eliminado Correctamente')
    return redirect(to="medico")


def eliminar_cliente(request, id_rut):
    cliente = get_object_or_404(Cliente, id_rut=id_rut)
    cliente.delete()
    messages.success(request, 'Cliente Eliminado Correctamente')
    return redirect(to="clientes")


def eliminar_paciente(request, id_pac):
    paciente = get_object_or_404(Paciente, id_pac=id_pac)
    paciente.delete()
    messages.success(request, 'Paciente Eliminado Correctamente')
    return redirect(to="pacientes")


@login_required()
def reservar_hdispo(request):
    reservar_hdispo = ReservaForm
    data = {
        'form': ReservaForm(instance=reservar_hdispo)
    }
    if request.method == 'POST':
        formulario = HrsDispoForm(
            data=request.POST, instance=reservar_hdispo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="horas_disponibles")
        data["form"] = formulario

    return render(request, 'modificar_hdisponible.html', data)


def procedimientos(request):
    busqueda = request.GET.get("buscar")
    print(busqueda)
    proced = ProcedPacien.objects.all()
    if busqueda:
        proced = ProcedPacien.objects.filter(
            
            Q(paciente_id_pac = busqueda)
    ).distinct()
       
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(proced, 7)
        proced = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': proced,
        'form':ProcedimientoPForm,
        'paginator': paginator
    }
    if request.method == 'POST':
        formulario = ProcedimientoPForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Procedimiento Agregado Correctamente")
            return redirect(to="procedimientos")

        data["form"] = formulario

    return render(request, 'procedimientos.html', data)

def custom_page_not_found_view(request, exception):
    return render(request, "em404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})