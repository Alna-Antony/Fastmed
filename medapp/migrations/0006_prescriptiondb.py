# Generated by Django 4.2.6 on 2023-11-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0005_delete_nondb'),
    ]

    operations = [
        migrations.CreateModel(
            name='prescriptiondb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.ImageField(blank=True, null=True, upload_to='prescriptionimages')),
            ],
        ),
    ]