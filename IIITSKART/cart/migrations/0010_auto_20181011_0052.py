# Generated by Django 2.1.1 on 2018-10-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20181011_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=70),
        ),
    ]