# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-20 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllParkingSpots',
            fields=[
                ('p_id', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=8, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableParkingSpots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(max_length=10)),
                ('parking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RideCellParkingApi.AllParkingSpots')),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=8, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='ReservedParkingSpots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_range', models.DateTimeField()),
                ('parking_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='RideCellParkingApi.AllParkingSpots')),
            ],
        ),
        migrations.AddField(
            model_name='availableparkingspots',
            name='place_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RideCellParkingApi.Places'),
        ),
    ]
