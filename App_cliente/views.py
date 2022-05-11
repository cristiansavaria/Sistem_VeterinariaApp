from django.shortcuts import render
from .forms import ContactoForm

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
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
            
    return render(request, 'contacto.html', data)

def quienes_somos(request):
    return render(request, 'quienes_somos.html')


def login(request):
    return render(request, 'login.html')
def historial(request):
    return render(request, 'historial.html')
def registro(request):
    return render(request, 'registro.html')