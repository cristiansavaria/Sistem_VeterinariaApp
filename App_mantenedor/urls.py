from django import views
from django.urls import path
from .views import clientes, index, insumos, pacientes, reserva_horas

urlpatterns = [
    path('index/', index, name='index'),
    path('clientes/', clientes, name='clientes'),
    path('pacientes/', pacientes, name='pacientes'),
    path('insumos/', insumos, name='insumos'),
    path('reserva_horas/', reserva_horas, name='reserva_horas'),
    
   
   
]