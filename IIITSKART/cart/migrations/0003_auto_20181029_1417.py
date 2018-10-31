# Generated by Django 2.1.1 on 2018-10-29 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20181029_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_wishlist',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 17, 11, 536357)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 17, 11, 536357)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 17, 11, 553361)),
        ),
        migrations.AlterField(
            model_name='order',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 17, 11, 553361)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 17, 11, 553361)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 17, 11, 553361)),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 17, 11, 553361)),
        ),
    ]
