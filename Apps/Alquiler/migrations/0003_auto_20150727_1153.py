# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0002_auto_20150727_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler_detail',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
