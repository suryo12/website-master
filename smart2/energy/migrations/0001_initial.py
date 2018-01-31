# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-24 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Node_ID', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NodeEnergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tegangan', models.CharField(max_length=100)),
                ('Energy', models.CharField(max_length=100)),
                ('Arus', models.CharField(max_length=100)),
                ('Frekuensi', models.CharField(max_length=100)),
                ('Total_energy', models.CharField(max_length=100)),
                ('Waktu', models.CharField(max_length=100)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.Node')),
            ],
        ),
    ]
