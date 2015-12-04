from django import forms

from .models import Egreso

class Egreso_Form(forms.ModelForm):

    class Meta:
        model = Egreso
        fields = ['fecha','asunto','valor']
        widgets = {
            'asunto':forms.TextInput(attrs = {
                'type':'text',
                'name':'asunto',
                'class':'form-control',
                'placeholder':'Ingrese el Asunto',
                'required':True
            }),
            'valor':forms.TextInput(attrs = {
                'type':'text',
                'name':'valor',
                'class':'form-control',
                'placeholder':'Ingrese el valor',
                'required':True
            }),
            'fecha': forms.DateInput(attrs={
                'type':'text',
                'class':'form-control',
                'name':'fecha_devolucion',
                'placeholder':'Ingrese Fecha ',
                'id':'prueba2'
            }),
        }