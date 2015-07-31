# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('full_nombre', models.CharField(max_length=100)),
                ('identificacion', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre_Empresa', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('personal_Responsable', models.CharField(max_length=100)),
                ('tipo_Proveedor', models.ManyToManyField(to='Inventario.Tipo')),
            ],
        ),
    ]
