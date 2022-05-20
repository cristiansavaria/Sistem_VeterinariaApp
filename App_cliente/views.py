from django.shortcuts import render
from .forms import ContactoForm, RegistroUsuario
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def base(request):
    return render(request, 'base.html')
def servicio(request):
    return render(request, 'servicios.html')
def reserva_hora(request):
    return render(request, 'reserva_hora.html')

def contacto(request):
    data = {
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            subject=request.POST["nombre"]
            message=request.POST["mensaje"] + " " + request.POST["correo"] + " " + request.POST["tipo_consulta"]
            email_from=settings.EMAIL_HOST_USER
            recipient_list=["clinica.huellitas2022@gmail.com"]
            send_mail(subject, message, email_from, recipient_list )

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
        
    return render(request, 'registration/registro.html', data)
   
    

def login(request):
    return render(request, 'registration/login.html')


def historial(request):
    return render(request, 'historial.html')




