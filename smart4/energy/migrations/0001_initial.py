# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-28 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Node_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Nama', models.CharField(max_length=640)),
                ('No_Telp', models.CharField(max_length=640)),
                ('Alamat', models.CharField(max_length=640)),
            ],
        ),
        migrations.CreateModel(
            name='EnergyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tegangan', models.CharField(max_length=1000)),
                ('Energy', models.CharField(max_length=1000)),
                ('Arus', models.CharField(max_length=1000)),
                ('Frekuensi', models.CharField(max_length=1000)),
                ('Total_energy', models.CharField(max_length=1000)),
                ('Waktu', models.CharField(max_length=1000)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.Customer')),
            ],
        ),
    ]
