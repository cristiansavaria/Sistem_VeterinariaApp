from dataclasses import field
from pyexpat import model
from django import forms 
from .models import AppClienteContacto, Cliente, Empleado, Insumo, Paciente


class InsumoForm(forms.ModelForm):

    class Meta:
        model = Insumo
        fields = '__all__'


class PacienteForm(forms.ModelForm):
     
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



