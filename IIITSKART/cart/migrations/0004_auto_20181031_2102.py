# Generated by Django 2.1.1 on 2018-10-31 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20181029_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 21, 2, 44, 868830)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 21, 2, 44, 868830)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 21, 2, 44, 870834)),
        ),
        migrations.AlterField(
            model_name='order',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 21, 2, 44, 870834)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 21, 2, 44, 870834)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 21, 2, 44, 869828)),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=230),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 21, 2, 44, 869828)),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]