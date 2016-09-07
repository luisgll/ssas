# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosTecnico',
            fields=[
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro')], max_length=1)),
                ('Telefono', models.CharField(max_length=11)),
                ('correo_corporativo', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=16)),
                ('fecha', models.DateField()),
                ('historico', models.TextField()),
                ('tecnico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repgar.DatosTecnico')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('serial', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('fecha2', models.DateField()),
                ('pantalla', models.BooleanField()),
                ('lector', models.BooleanField()),
                ('memoria_ram', models.BooleanField()),
                ('fan_cooler', models.BooleanField()),
                ('computadora', models.BooleanField()),
                ('ele', models.BooleanField()),
                ('tecnico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repgar.DatosTecnico')),
            ],
        ),
    ]