# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0002_auto_20150803_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='abono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='reserva',
            field=models.BooleanField(default=False),
        ),
    ]
