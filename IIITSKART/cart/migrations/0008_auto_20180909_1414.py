# Generated by Django 2.1.1 on 2018-09-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20180908_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='created',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='login',
            name='modified',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=70, null=True, unique=True),
        ),
    ]
