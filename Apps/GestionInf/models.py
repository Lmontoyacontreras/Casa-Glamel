from django.db import models

from Apps.Inventario.models import Tipo

class Proveedor(models.Model):
    nombre_Empresa= models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    personal_Responsable = models.CharField(max_length=100)
    tipo_Proveedor = models.ManyToManyField(Tipo)

    def __str__(self):
        return self.nombre_Empresa


