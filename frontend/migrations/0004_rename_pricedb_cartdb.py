# Generated by Django 4.2.6 on 2023-11-23 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_pricedb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pricedb',
            new_name='cartdb',
        ),
    ]