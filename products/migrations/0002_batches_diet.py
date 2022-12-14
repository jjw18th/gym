# Generated by Django 3.2.7 on 2022-01-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchName', models.CharField(max_length=200)),
                ('BatchTiming', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meal', models.CharField(max_length=200)),
                ('Time', models.IntegerField()),
                ('WhatToEat', models.CharField(max_length=500)),
            ],
        ),
    ]
