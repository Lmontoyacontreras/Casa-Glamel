# -*- coding: utf-8 -*-
from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    famila_idfamilia = models.ForeignKey(Familia)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre_tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_tipo

class Estado(models.Model):
    nombre_estado = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_estado

class Estado_Ropa(models.Model):
    nombre_estado_ropa = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_estado_ropa

class Color(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color

class Talla (models.Model):
    talla = models.CharField(max_length=2)

    def __str__(self):
        return self.talla


class Articulo(models.Model):
    categoria_idcategoria = models.ForeignKey(Categoria)
    nombre_tipo = models.ForeignKey(Tipo)
    nombre_estado = models.ForeignKey(Estado)
    nombre_estado_ropa = models.ForeignKey(Estado_Ropa)
    color = models.ForeignKey(Color)
    referencia = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    fechaingreso = models.DateField()
    fechautil = models.DateField()
    precio = models.IntegerField()
    ubicacion = models.CharField(max_length=45)
    talla = models.ForeignKey(Talla)


    def __str__(self):
        return self.referencia
