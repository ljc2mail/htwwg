# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.TextField()),
                ('fin_type', models.CharField(choices=[('Falcate', 'falcate'), ('Traiangular', 'triangular'), ('Rounded', 'rounded')], max_length=30)),
                ('whale_type', models.CharField(choices=[('Humpback', 'humpback'), ('Orca', 'orca')], max_length=30)),
                ('blow_type', models.CharField(choices=[('Tall', 'tall'), ('Bushy', 'bushy'), ('Dense', 'dense')], max_length=30)),
                ('wave_type', models.CharField(choices=[('Flat', 'flat'), ('Small', 'small'), ('High', 'high')], max_length=30)),
            ],
        ),
    ]
