# Generated by Django 2.1.2 on 2018-12-09 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20181209_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 11, 54, 44, 657977)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 11, 54, 44, 657977)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 11, 54, 44, 662009)),
        ),
        migrations.AlterField(
            model_name='order',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 11, 54, 44, 662009)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 11, 54, 44, 662009)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 11, 54, 44, 657977)),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 11, 54, 44, 657977)),
        ),
    ]
