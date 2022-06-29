from django.shortcuts import get_object_or_404, redirect, render
from App_mantenedor.forms import ReservaForm
from App_mantenedor.models import HrsDispo, Reserva
from .forms import ContactoForm, RegistroUsuario
from django.core.mail import send_mail
from django.conf import settings
from .models import Contacto
from django.contrib import messages
# Create your views here.
from App_mantenedor.views import  reservar_hdispo

def base(request):
    return render(request, 'base.html')


def servicio(request):
    return render(request, 'servicios.html')


def reserva_hora(request):
    return render(request, 'reserva_hora.html')


def contacto(request):

    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Formulario Enviado Correctamente")
            # subject=request.POST["tipo_consulta"]
            #message=request.POST["mensaje"] + "--- mi correo es --- " + request.POST["correo"] + " --- mi nombre es ---  " + request.POST["nombre"]
            # email_from=settings.EMAIL_HOST_USER
            # recipient_list=["clinica.huellitas2022@gmail.com"]
            #send_mail(subject, message, email_from, recipient_list )

            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'contacto.html', data)


def quienes_somos(request):
    return render(request, 'quienes_somos.html')


def registro(request):
    data = {
        'form': RegistroUsuario()
    }
    if request.method == 'POST':
        formulario = RegistroUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()

        data["form"] = formulario

    return render(request, 'registro.html', data)


def login(request):
    return render(request, 'login.html')


def historial(request):
    return render(request, 'historial.html')


def resv_hora(request):
    disp = HrsDispo.objects.all().filter(activo=1)

    data = {
        'disp': disp,
    }
    return render(request, 'resv_hora.html', data)


def detalle_reserva(request, idhrs_dispo):
    horasdisponibles = get_object_or_404(HrsDispo, idhrs_dispo=idhrs_dispo)
    reserva = Reserva.objects.all()
    data = {
        'reserva': reserva,
        'form': ReservaForm(instance=horasdisponibles)
    }
    if request.method == 'POST':
        formulario = ReservaForm(
            data=request.POST)
        if formulario.is_valid():
            formulario.save()
            horasdisponibles.delete()
            return redirect(to="resv_hora")
        data["form"] = formulario

    return render(request, 'reservarCliente.html', data)