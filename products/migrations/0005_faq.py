# Generated by Django 3.2.7 on 2022-01-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Query', models.CharField(max_length=300)),
                ('Response', models.CharField(max_length=300)),
            ],
        ),
    ]
