# Generated by Django 2.1.1 on 2018-09-05 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='c_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('blacklist', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.customer')),
            ],
        ),
        migrations.AddField(
            model_name='c_review',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.customer'),
        ),
        migrations.AddField(
            model_name='admin',
            name='a_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.login'),
        ),
    ]
