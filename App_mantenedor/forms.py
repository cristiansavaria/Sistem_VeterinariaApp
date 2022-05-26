from dataclasses import field
from pyexpat import model
from django import forms 
from .models import Insumo, Paciente


class InsumoForm(forms.ModelForm):

    class Meta:
        model = Insumo
        fields = '__all__'


class PacienteForm(forms.ModelForm):
     
     class Meta:
         model = Paciente
         fields = '__all__'




