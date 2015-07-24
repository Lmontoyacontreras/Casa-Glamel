# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='factura_Proveedor',
            field=models.ForeignKey(to='ControlProv.Factura_Provedor'),
        ),
    ]
