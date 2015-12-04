__author__ = 'Usuario'
from django import forms

from .models import Reserva,Reserva_Detail

class Reserva_Form(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['vendedor','cliente','fecha_reserva','fecha_limite','abono_inicial','descuento']
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
            'descuento': forms.TextInput(attrs={
                'type':'text',
                'name':'referencia',
                'class':'form-control',
                'placeholder':'Descuento',
            }),
        }

class Reserva_Form_Abono(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['abono_inicial']
        widgets = {
            'abono_inicial': forms.TextInput(attrs={
                'type':'text',
                'name':'referencia',
                'class':'form-control',
                'placeholder':'Abono Inicial',
            }),
        }

class Reserva_Detail_Form(forms.ModelForm):
    class Meta:
        model = Reserva_Detail
        fields=['articulo','gratis']
        widgets = {
            'articulo':forms.Select(attrs={
                'class':'form-control chosen-select'
            })
        }