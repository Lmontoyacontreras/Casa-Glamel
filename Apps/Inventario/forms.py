__author__ = 'Usuario'
# -*- coding: utf-8 -*-
from django import forms

from .models import Familia,Categoria,Articulo

class Familia_Form(forms.ModelForm):

    class Meta:
        model = Familia
        fields = ['nombre','descripcion']
        widgets = {
            'nombre':forms.TextInput(attrs = {
                'type':'text',
                'name':'nombre',
                'class':'form-control',
                'placeholder':'Ingrese el nombre de la Familia'
            }),
            'descripcion': forms.Textarea(attrs = {
                'class':'form-control',
                'row':'5',
                'placeholder':'Describa la Familia'
            }),
        }


class Categoria_Form(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('nombre', 'famila_idfamilia','descripcion')
        widgets = {
            'nombre' : forms.TextInput(attrs = {
                'type':'text',
                'name':'nombre',
                'class':'form-control',
                'placeholder':'Ingrese el nombre de la Categoria'
            }),
            'famila_idfamilia' : forms.Select(attrs={
                'class':'form-control'
            }),
            'descripcion': forms.Textarea(attrs = {
                'class':'form-control',
                'row':'5',
                'placeholder':'Describa la Categoria'
            }),
        }

class Articulo_Form(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ('categoria_idcategoria','nombre_tipo','nombre_estado_ropa',
                  'nombre_estado','referencia', 'descripcion', 'fechaingreso',
                  'fechautil','precio','ubicacion','color','talla')

        widgets = {
            'fechaingreso': forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'dd/mm/yyyy',
            }),
            'fechautil': forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'dd/mm/yyyy',
            }),
            'talla': forms.Select(attrs={
                'class':'form-control'
            }),
            'categoria_idcategoria': forms.Select(attrs={
                'class':'form-control'
            }),
            'nombre_tipo':forms.Select(attrs={
                'class':'form-control'
            }),
            'referencia':forms.TextInput(attrs={
                'type':'text',
                'name':'referencia',
                'class':'form-control',
                'placeholder':'Ingrese referencia del articulo',
            }),
            'descripcion': forms.Textarea(attrs = {
                'class':'form-control',
                'row':'5',
                'placeholder':'Describa la Categoria'
            }),
            'nombre_estado_ropa':forms.Select(attrs={
                'class':'form-control'
            }),
            'nombre_estado':forms.Select(attrs={
                'class':'form-control'
            }),
            'color':forms.Select(attrs={
                'class':'form-control'
            }),
            'ubicacion':forms.TextInput(attrs={
                'type':'text',
                'name':'referencia',
                'class':'form-control',
                'placeholder':'Ingrese ubicacion del articulo',
            }),
            'precio':forms.TextInput(attrs={
                'type':'text',
                'name':'referencia',
                'class':'form-control',
                'placeholder':'Ingrese precio del articulo',
            }),

        }
