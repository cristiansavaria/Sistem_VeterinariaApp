from django import views
from django.urls import path
from .views import clientes, index, insumos, login_admin, modificar_cliente, modificar_insumo, modificar_medico, modificar_paciente, pacientes, reserva_horas, medico

urlpatterns = [
    path('index/', index, name='index'),
    path('clientes/', clientes, name='clientes'),
    path('pacientes/', pacientes, name='pacientes'),
    path('medico/', medico, name='medico'),
    path('insumos/', insumos, name='insumos'),
    path('reserva_horas/', reserva_horas, name='reserva_horas'),
    path('modificar_insumo/<id_insumo>/', modificar_insumo, name="modificar_insumo"), 
    path('modificar_cliente/<id_rut>/', modificar_cliente, name="modificar_cliente"), 
    path('modificar_medico/<id_emp>/', modificar_medico, name="modificar_medico"), 
    path('modificar_paciente/<id_pac>/', modificar_paciente, name="modificar_paciente"), 
    path('login_admin/', login_admin, name='login_admin'),
    
   
   
]