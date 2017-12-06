# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='D',
            fields=[
                ('numero', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('piso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rut', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellidomaterno', models.CharField(max_length=50)),
                ('apellidopaterno', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=20, choices=[('dueño', 'dueño'), ('arrendatario', 'arrendatario')])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechavigencia', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='d',
            name='residente',
            field=models.ForeignKey(to='ApiRestEdif.Residente'),
        ),
    ]
