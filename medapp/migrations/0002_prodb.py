# Generated by Django 4.2.6 on 2023-11-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prodb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(blank=True, max_length=100, null=True)),
                ('productname', models.CharField(blank=True, max_length=100, null=True)),
                ('productdescription', models.CharField(blank=True, max_length=100, null=True)),
                ('productprice', models.IntegerField(blank=True, null=True)),
                ('productimage', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]