from django import forms

from .models import Alquiler,Alquiler_Detail
from Apps.GestionInf.models import Cliente

class Alquiler_Form(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ['vendedor','cliente','fecha_entrega','fecha_devolucion','deposito','observaciones','descuento']
        widgets = {
            'cliente': forms.Select(attrs={
                'class':'form-control chosen-select'
            }),
            'fecha_entrega': forms.DateInput(attrs={
                'type':'text',
                'name':'fecha_entrega',
                'class':'form-control',
                'placeholder':'Ingrese Fecha Entrega',
                'id':'prueba'
            }),
            'fecha_devolucion': forms.DateInput(attrs={
                'type':'text',
                'class':'form-control',
                'name':'fecha_devolucion',
                'placeholder':'Ingrese Fecha Devolucion',
                'id':'prueba2'
            }),
            'deposito': forms.TextInput(attrs={
                'type':'text',
                'name':'referencia',
                'class':'form-control',
                'placeholder':'Deposito',
            }),
            'descuento': forms.TextInput(attrs={
                'type':'text',
                'name':'referencia',
                'class':'form-control',
                'placeholder':'Descuento',
            }),
            'observaciones': forms.Textarea(attrs={
                'class':'form-control',
                'row':'3',
                'placeholder':'Observaciones',
            }),
        }


class Alquiler_Detail_Form(forms.ModelForm):
    class Meta:
        model = Alquiler_Detail
        fields=['articulo','gratis','precio']
        widgets = {
            'articulo':forms.Select(attrs={
                'class':'form-control chosen-select',
                'required':True,
            })
        }


class Alquiler_Reserva_Form(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ['vendedor','cliente','fecha_entrega','fecha_devolucion','deposito','observaciones','descuento']
        widgets = {
            'fecha_devolucion': forms.DateInput(attrs={
                'type':'text',
                'class':'form-control',
                'name':'fecha_devolucion',
                'placeholder':'Ingrese Fecha Devolucion',
                'id':'prueba2',
                'required' : True
            }),
            'deposito': forms.TextInput(attrs={
                'type':'text',
                'name':'referencia',
                'class':'form-control',
                'placeholder':'Deposito',
                'required' : True
            }),
            'observaciones': forms.Textarea(attrs={
                'class':'form-control',
                'row':'3',
                'placeholder':'Observaciones',
                'required' : True
            }),
        }