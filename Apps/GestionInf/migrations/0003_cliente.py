# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionInf', '0002_auto_20150716_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('full_nombre', models.CharField(max_length=100)),
                ('identificacion', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
    ]
