# Generated by Django 3.2.7 on 2021-11-13 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_userdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='Userdetail',
        ),
    ]
