from dataclasses import field
from pyexpat import model
from django import forms 
from .models import AppClienteContacto, Cliente, Empleado, Insumo, Paciente, Reserva,  HrsDispo, ProcedPacien
import datetime

class InsumoForm(forms.ModelForm):

    class Meta:
        model = Insumo
        fields = '__all__'


class PacienteForm(forms.ModelForm):
     fecha_actual = datetime.datetime.today().year
     rango_anio = tuple([i for i in range(fecha_actual - 15, fecha_actual + 1)])
     fec_nac = forms.DateField(widget=forms.SelectDateWidget(years=rango_anio))
     class Meta:
         model = Paciente
         fields = '__all__'
        

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

class MedicoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'

class ContactoRForm(forms.ModelForm):
    class Meta:
        model = AppClienteContacto
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    fecha_actual = datetime.datetime.today().year
    rango_anio = tuple([i for i in range(fecha_actual - 0, fecha_actual + 1)])
    fec_res = forms.DateField(widget=forms.SelectDateWidget(years=rango_anio))
    class Meta:
        model = Reserva
        fields = '__all__'


class HrsDispoForm(forms.ModelForm):

    class Meta:
        model = HrsDispo
        fields = '__all__'

class ProcedimientoPForm(forms.ModelForm):

    class Meta:
        model = ProcedPacien
        fields = '__all__'


