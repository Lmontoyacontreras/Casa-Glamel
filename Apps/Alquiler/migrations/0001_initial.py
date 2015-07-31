# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionInf', '0001_initial'),
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('vendedor', models.CharField(blank=True, max_length=50)),
                ('fecha_entrega', models.DateField()),
                ('fecha_devolucion', models.DateField()),
                ('devuelto', models.BooleanField(default=False)),
                ('deposito', models.IntegerField()),
                ('observaciones', models.TextField()),
                ('cliente', models.ForeignKey(to='GestionInf.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('gratis', models.BooleanField(default=False)),
                ('precio', models.IntegerField()),
                ('alquiler', models.ForeignKey(to='Alquiler.Alquiler')),
                ('articulo', models.ForeignKey(to='Inventario.Articulo')),
            ],
        ),
    ]
