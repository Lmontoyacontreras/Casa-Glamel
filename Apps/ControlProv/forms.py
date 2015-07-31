from django import forms

from .models import Factura_Provedor,Pedido

class Factura_Provedor_Form(forms.ModelForm):

    class Meta:
        model = Factura_Provedor
        fields = ['nombre_Empresa','fecha_Pedido','fecha_Pago','estado']
        widgets = {
            'nombre_Empresa':forms.Select(attrs={
                'class':'form-control',
            }),
            'estado':forms.Select(attrs={
                'class':'form-control',
            }),
            'fecha_Pedido':forms.DateInput(attrs={
                'type':'text',
                'class':'form-control',
                'placeholder':'Ingrese Fecha Pedido',
                'id':'prueba'
            }),
            'fecha_Pago':forms.DateInput(attrs={
                'type':'text',
                'class':'form-control',
                'placeholder':'Ingrese Fecha Pago',
                'id':'prueba2'
            }),
        }


class Pedido_Form(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_Articulo','descripcion','cantidad','precio']
        widgets = {
            'nombre_Articulo' : forms.TextInput(attrs = {
                'type':'text',
                'name':'nombre',
                'class':'form-control',
                'placeholder':'Ingrese el nombre Del Articulo'
            }),
            'descripcion': forms.Textarea(attrs = {
                'class':'form-control',
                'row':'5',
                'placeholder':'Describa el articulo'
            }),
            'cantidad' : forms.TextInput(attrs = {
                'type':'text',
                'name':'nombre',
                'class':'form-control',
                'placeholder':'Ingrese la cantidad'
            }),
            'precio' : forms.TextInput(attrs = {
                'type':'text',
                'name':'nombre',
                'class':'form-control',
                'placeholder':'Ingrese el precio por unidad'
            }),
        }