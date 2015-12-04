from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.urlresolvers import reverse

from Apps.GestionInf.models import Cliente
from Apps.Inventario.models import Articulo

# Create your models here.

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente)
    vendedor = models.CharField(max_length=50,blank=True)
    fecha_reserva = models.DateField()
    fecha_limite = models.DateField()
    abono_inicial = models.IntegerField()
    descuento = models.IntegerField(default=0, null=True, blank=True, validators=[
                                        MinValueValidator(0),
                                        MaxValueValidator(100)
                                    ])

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('Reservas:Reserva_Detail_Ingresar',kwargs={'pk':self.pk})

class Reserva_Detail(models.Model):
    reserva = models.ForeignKey(Reserva)
    articulo = models.ForeignKey(Articulo)
    gratis = models.BooleanField(default=False)

    def __str__(self):
        return str(self.articulo)

