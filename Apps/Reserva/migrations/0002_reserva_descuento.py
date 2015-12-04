# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='descuento',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
