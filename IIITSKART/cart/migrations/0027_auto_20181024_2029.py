# Generated by Django 2.1.1 on 2018-10-24 14:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0026_auto_20181024_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(default='media/default-user.png', storage='/media/profile', upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 20, 29, 20, 610143)),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='cart.Product'),
        ),
        migrations.AlterField(
            model_name='p_review',
            name='pro_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Product'),
        ),
    ]
