# Generated by Django 2.1.1 on 2018-10-22 11:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0022_auto_20181022_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(default='media/default-user.png', upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 22, 16, 47, 37, 237676)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Product'),
        ),
        migrations.AlterField(
            model_name='p_review',
            name='pro_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Product'),
        ),
    ]
