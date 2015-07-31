# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionInf', '0002_auto_20150716_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Factura_Provedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fecha_Pedido', models.DateField()),
                ('fecha_Pago', models.DateField()),
                ('estado', models.ForeignKey(to='ControlProv.Estado')),
                ('nombre_Empresa', models.ForeignKey(to='GestionInf.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre_Articulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('factura_Proveedor', models.ForeignKey(to='GestionInf.Proveedor', blank=True)),
            ],
        ),
    ]
