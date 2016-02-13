# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionInf', '0002_cliente_peligroso'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='numeros_compras',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
