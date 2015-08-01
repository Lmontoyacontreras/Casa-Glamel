# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nuevo', models.BooleanField(default=False)),
                ('referencia', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=100)),
                ('fechaingreso', models.DateField()),
                ('fechautil', models.DateField()),
                ('precio_original', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=100)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre_estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Ropa',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre_estado_ropa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('talla', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre_tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='famila_idfamilia',
            field=models.ForeignKey(to='Inventario.Familia'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria_idcategoria',
            field=models.ForeignKey(to='Inventario.Categoria'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='color',
            field=models.ForeignKey(to='Inventario.Color'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='nombre_estado',
            field=models.ForeignKey(to='Inventario.Estado'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='nombre_estado_ropa',
            field=models.ForeignKey(to='Inventario.Estado_Ropa'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='nombre_tipo',
            field=models.ForeignKey(to='Inventario.Tipo'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='talla',
            field=models.ForeignKey(to='Inventario.Talla'),
        ),
    ]
