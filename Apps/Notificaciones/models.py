# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Notificaciones(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre

