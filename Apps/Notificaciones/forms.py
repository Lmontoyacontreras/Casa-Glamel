from django import forms

from .models import Notificaciones

class Notificaciones_Form(forms.ModelForm):

    class Meta:
        model = Notificaciones
        fields = ['nombre','descripcion']
        widgets = {
            'nombre':forms.TextInput(attrs = {
                'type':'text',
                'name':'nombre',
                'class':'form-control',
                'placeholder':'Ingrese el Asunto',
                'required':True
            }),
            'descripcion': forms.Textarea(attrs = {
                'class':'form-control',
                'row':'5',
                'placeholder':'Describa el asunto',
                'required':True
            }),
        }