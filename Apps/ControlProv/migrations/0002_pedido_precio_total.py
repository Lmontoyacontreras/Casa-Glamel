# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='precio_total',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
