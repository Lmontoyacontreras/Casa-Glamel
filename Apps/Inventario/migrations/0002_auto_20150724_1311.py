# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='nuevo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='articulo',
            name='precio_original',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
