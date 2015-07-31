# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0007_auto_20150727_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler_detail',
            name='alquiler',
            field=models.ForeignKey(null=True, to='Alquiler.Alquiler', blank=True),
        ),
    ]
