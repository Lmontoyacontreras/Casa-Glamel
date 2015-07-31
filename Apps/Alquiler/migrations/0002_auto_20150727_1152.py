# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler_detail',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='devuelto',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='vendedor',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
