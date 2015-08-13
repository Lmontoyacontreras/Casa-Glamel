# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='fecha_devolucion_dia',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='multa',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
