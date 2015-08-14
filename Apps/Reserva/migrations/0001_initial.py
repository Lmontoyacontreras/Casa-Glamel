# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
        ('GestionInf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('vendedor', models.CharField(max_length=50, blank=True)),
                ('fecha_reserva', models.DateField()),
                ('fecha_limite', models.DateField()),
                ('abono_inicial', models.IntegerField()),
                ('cliente', models.ForeignKey(to='GestionInf.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('gratis', models.BooleanField(default=False)),
                ('articulo', models.ForeignKey(to='Inventario.Articulo')),
                ('reserva', models.ForeignKey(to='Reserva.Reserva')),
            ],
        ),
    ]
