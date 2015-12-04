from django.db import models

class Egreso(models.Model):
    fecha = models.DateField()
    asunto = models.CharField(max_length=100)
    valor = models.IntegerField()

    def __str__(self):
        return self.asunto