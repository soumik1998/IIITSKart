# Generated by Django 2.1.1 on 2018-10-24 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 25, 2, 34, 48, 255867)),
        ),
    ]
