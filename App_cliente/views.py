from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')
def servicio(request):
    return render(request, 'servicios.html')
def reserva_hora(request):
    return render(request, 'reserva_hora.html')
def contacto(request):
    return render(request, 'contacto.html')
def quienes_somos(request):
    return render(request, 'quienes_somos.html')
