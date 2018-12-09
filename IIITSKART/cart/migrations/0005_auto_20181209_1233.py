# Generated by Django 2.1.2 on 2018-12-09 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20181209_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 12, 33, 45, 956266)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 12, 33, 45, 957265)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 12, 33, 45, 959257)),
        ),
        migrations.AlterField(
            model_name='order',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 12, 33, 45, 959257)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 12, 33, 45, 958260)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 12, 33, 45, 958260)),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 12, 33, 45, 958260)),
        ),
    ]