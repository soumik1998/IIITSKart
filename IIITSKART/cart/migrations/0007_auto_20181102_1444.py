# Generated by Django 2.1.2 on 2018-11-02 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20181102_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 14, 44, 8, 552176)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 14, 44, 8, 553174)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 14, 44, 8, 554171)),
        ),
        migrations.AlterField(
            model_name='order',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 14, 44, 8, 554171)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 14, 44, 8, 554171)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 14, 44, 8, 554171)),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 14, 44, 8, 554171)),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
