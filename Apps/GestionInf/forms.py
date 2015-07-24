from django import forms

from .models import Proveedor

class Proveedor_Form(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['nombre_Empresa','nit','telefono','direccion',
                  'correo','personal_Responsable','tipo_Proveedor']
        widgets = {
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