__author__ = 'Usuario'
from django import forms

from .models import Reserva

class Reserva_Form(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['vendedor','cliente','fecha_reserva','fecha_limite','abono_inicial']
        widgets = {
            'cliente':forms.Select(attrs={
                'class':'form-control chosen-select'
            }),
             'fecha_reserva': forms.DateInput(attrs={
                'type':'text',
                'name':'fecha_reserva',
                'class':'form-control',
                'placeholder':'Ingrese Fecha Entrega',
                'id':'prueba'
            }),
             'fecha_limite': forms.DateInput(attrs={
                'type':'text',
                'name':'fecha_limite',
                'class':'form-control',
                'placeholder':'Ingrese Fecha Cancelacion',
                'id':'prueba2'
            }),
            'abono_inicial': forms.TextInput(attrs={
                'type':'text',
                'name':'referencia',
                'class':'form-control',
                'placeholder':'Abono Inicial',
            }),
        }