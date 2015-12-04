# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionInf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='peligroso',
            field=models.BooleanField(default=False),
        ),
    ]
