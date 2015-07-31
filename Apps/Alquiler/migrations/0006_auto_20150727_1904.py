# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0005_auto_20150727_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler_detail',
            name='gratis',
            field=models.BooleanField(default=True),
        ),
    ]
