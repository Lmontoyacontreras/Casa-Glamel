# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0003_auto_20150727_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='fecha_devolucion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='fecha_entrega',
            field=models.DateField(),
        ),
    ]
