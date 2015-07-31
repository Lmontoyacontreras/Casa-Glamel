from django.db import models
from django.core.urlresolvers import reverse

from Apps.GestionInf.models import Proveedor


class Estado(models.Model):
    nombre_estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_estado

class Factura_Provedor(models.Model):
    nombre_Empresa = models.ForeignKey(Proveedor)
    fecha_Pedido = models.DateField()
    fecha_Pago = models.DateField()
    estado = models.ForeignKey(Estado)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('ControlProv:Pedido_Ingresar',kwargs={'pk':self.pk})

class Pedido(models.Model):
    factura_Proveedor = models.ForeignKey(Factura_Provedor)
    nombre_Articulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre_Articulo
