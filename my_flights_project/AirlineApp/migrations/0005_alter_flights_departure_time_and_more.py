# Generated by Django 4.2.1 on 2023-06-03 17:29

import AirlineApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineApp', '0004_flights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='departure_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flights',
            name='landing_time',
            field=models.DateTimeField(),
        ),
    ]