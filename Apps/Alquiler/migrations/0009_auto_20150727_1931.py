# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0008_auto_20150727_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler_detail',
            name='alquiler',
            field=models.ForeignKey(to='Alquiler.Alquiler'),
        ),
    ]
