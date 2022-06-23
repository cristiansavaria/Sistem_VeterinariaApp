from django import views
from django.urls import path


from .views import clientes, contacto_recibido,error_404, eliminar_cliente, modificar_proced, procedimientos,\
 eliminar_empleado, eliminar_insumo, eliminar_paciente, index, insumos, login, modificar_cliente, modificar_insumo,\
  modificar_medico, modificar_paciente, modificar_reserva, pacientes, reserva_horas, medico, horas_disponibles,\
   modificar_hdisponible, reservar_hdispo

urlpatterns = [
    path('index/', index, name='index'),
    path('clientes/', clientes, name='clientes'),
    path('pacientes/', pacientes, name='pacientes'),
    path('medico/', medico, name='medico'),
    path('insumos/', insumos, name='insumos'),
    path('reserva_horas/', reserva_horas, name='reserva_horas'),
    path('horas_disponibles/', horas_disponibles, name="horas_disponibles"), 
    path('modificar_insumo/<id_insumo>/', modificar_insumo, name="modificar_insumo"), 
    path('modificar_cliente/<id_rut>/', modificar_cliente, name="modificar_cliente"), 
    path('modificar_medico/<id_emp>/', modificar_medico, name="modificar_medico"), 
    path('modificar_paciente/<id_pac>/', modificar_paciente, name="modificar_paciente"), 
    path('modificar_reserva/<id_res>/', modificar_reserva, name="modificar_reserva"), 
    path('modificar_proced/<idpro_pac>/', modificar_proced, name="modificar_proced"), 
    path('modificar_hdisponible/<idhrs_dispo>/', modificar_hdisponible, name="modificar_hdisponible"), 
    path('contacto_recibido/',contacto_recibido, name='recibidos' ),
    path('login/', login, name='login'),
    path('eliminar-insumo/<id_insumo>/', eliminar_insumo, name="eliminar_insumo"), 
    path('eliminar-medico/<id_emp>/', eliminar_empleado, name="eliminar_medico"), 
    path('eliminar-cliente/<id_rut>/', eliminar_cliente, name="eliminar_cliente"), 
    path('eliminar-paciente/<id_pac>/', eliminar_paciente, name="eliminar_paciente"),
    path('procedimientos/', procedimientos, name="procedimientos"),
    path('em404/', error_404, name="em404"),

   
   
]