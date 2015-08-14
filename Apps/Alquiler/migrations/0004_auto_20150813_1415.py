# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0003_auto_20150813_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alquiler',
            name='abono',
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='reserva',
        ),
    ]
