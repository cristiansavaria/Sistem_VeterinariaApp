from django import views
from django.urls import path


from .views import base, detalle_reserva, historial, login, registro, resv_hora, servicio, reserva_hora, contacto, quienes_somos


urlpatterns = [
    path('', base, name='inicio'),
    path('servicio/', servicio, name='servicio'),
    path('reserva_hora/', reserva_hora, name='reserva_hora'),
    path('contacto/', contacto, name='contacto'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('historial/', historial, name='historial'),
    path('resv_hora/', resv_hora, name='resv_hora'),
    path('reservarCliente/<idhrs_dispo>/', detalle_reserva, name='reservarCliente'),
]