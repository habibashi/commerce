# Generated by Django 2.2.12 on 2022-07-18 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreateList',
            new_name='Listing',
        ),
    ]
