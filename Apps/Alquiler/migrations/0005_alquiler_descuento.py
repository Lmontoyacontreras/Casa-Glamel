# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0004_auto_20150813_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='descuento',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], default=0, blank=True, null=True),
        ),
    ]
