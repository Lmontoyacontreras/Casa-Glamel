# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0005_auto_20150724_1319'),
        ('GestionInf', '0003_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('vendedor', models.CharField(max_length=50)),
                ('fecha_entrega', models.DateTimeField()),
                ('fecha_devolucion', models.DateTimeField()),
                ('devuelto', models.NullBooleanField()),
                ('deposito', models.IntegerField()),
                ('observaciones', models.TextField()),
                ('cliente', models.ForeignKey(to='GestionInf.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gratis', models.BooleanField(default=False)),
                ('alquiler', models.ForeignKey(to='Alquiler.Alquiler')),
                ('articulo', models.ForeignKey(to='Inventario.Articulo')),
            ],
        ),
    ]
