# Generated by Django 3.2.7 on 2022-01-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='Pic',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
