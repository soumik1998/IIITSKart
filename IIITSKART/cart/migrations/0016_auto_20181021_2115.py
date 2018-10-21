# Generated by Django 2.1.1 on 2018-10-21 15:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0015_auto_20181014_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='c_id',
        ),
        migrations.RemoveField(
            model_name='super_user',
            name='a_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 21, 21, 15, 1, 936343)),
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
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='super_user',
        ),
    ]