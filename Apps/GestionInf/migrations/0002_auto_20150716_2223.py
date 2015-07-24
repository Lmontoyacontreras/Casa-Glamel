# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
        ('GestionInf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='articulo_Proveedor',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tipo_Proveedor',
            field=models.ManyToManyField(to='Inventario.Tipo'),
        ),
        migrations.DeleteModel(
            name='Articulo_Proveedor',
        ),
    ]
