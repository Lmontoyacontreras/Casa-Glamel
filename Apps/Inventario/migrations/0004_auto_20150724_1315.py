# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_auto_20150724_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='nuevo',
            field=models.BooleanField(default=True),
        ),
    ]
