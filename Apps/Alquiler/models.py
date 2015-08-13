from django.db import models
from django.core.urlresolvers import reverse

from Apps.GestionInf.models import Cliente
from Apps.Inventario.models import Articulo


class Alquiler(models.Model):
    cliente = models.ForeignKey(Cliente)
    vendedor = models.CharField(max_length=50,blank=True)
    fecha_entrega = models.DateField()
    fecha_devolucion = models.DateField()
    devuelto = models.BooleanField(default=False)
    deposito = models.IntegerField()
    observaciones = models.TextField()
    fecha_devolucion_dia = models.DateField(blank=True,null=True)
    multa = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('Alquiler:Alquiler_Detail_Ingresar',kwargs={'pk':self.pk})


class Alquiler_Detail(models.Model):
    articulo = models.ForeignKey(Articulo)
    alquiler = models.ForeignKey(Alquiler)
    gratis = models.BooleanField(default=False)
    precio = models.IntegerField()

    def __str__(self):
        return str(self.articulo)