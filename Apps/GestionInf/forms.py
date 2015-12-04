from django import forms

from .models import Proveedor,Cliente

class Proveedor_Form(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['nombre_Empresa','nit','telefono','direccion',
                  'correo','personal_Responsable','tipo_Proveedor']
        widgets = {
            'tipo_Proveedor': forms.SelectMultiple(attrs={
                'class':'form-control'
            }),
            'nombre_Empresa':forms.TextInput(attrs={
                'type':'text',
                'name':'nombre_Empresa',
                'class':'form-control',
                'placeholder':'Ingrese el nombre de la Empresa'
            }),
            'nit':forms.TextInput(attrs={
                'type':'text',
                'name':'nombre_Empresa',
                'class':'form-control',
                'placeholder':'Ingrese el nit de la Empresa'
            }),
            'telefono':forms.TextInput(attrs={
                'type':'text',
                'name':'nombre_Empresa',
                'class':'form-control',
                'placeholder':'Ingrese el telefono de la Empresa'
            }),
            'direccion':forms.TextInput(attrs={
                'type':'text',
                'name':'nombre_Empresa',
                'class':'form-control',
                'placeholder':'Ingrese el direccion de la Empresa'
            }),
            'correo':forms.TextInput(attrs={
                'type':'text',
                'name':'nombre_Empresa',
                'class':'form-control',
                'placeholder':'Ingrese el correo de la Empresa'
            }),
            'personal_Responsable':forms.TextInput(attrs={
                'type':'text',
                'name':'nombre_Empresa',
                'class':'form-control',
                'placeholder':'Ingrese el contacto de la Empresa'
            }),
        }


class Cliente_Form(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['full_nombre','identificacion','direccion','telefono','correo','peligroso']
        widgets = {
            'full_nombre':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control',
                'placeholder':'Ingrese el nombre y apellido'
            }),
            'identificacion':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control',
                'placeholder':'Ingrese el numero de identificacion'
            }),
            'direccion':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control',
                'placeholder':'Ingrese direccion del cliente'
            }),
            'telefono':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control',
                'placeholder':'Ingrese el celular o telefono'
            }),
            'correo':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control',
                'placeholder':'Ingrese correo'
            }),
        }