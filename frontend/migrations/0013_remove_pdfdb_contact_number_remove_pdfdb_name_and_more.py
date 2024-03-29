# Generated by Django 4.2.6 on 2023-12-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_remove_pdfdb_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfdb',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='pdfdb',
            name='name',
        ),
        migrations.AddField(
            model_name='pdfdb',
            name='firstname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pdfdb',
            name='lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pdfdb',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pdfdb',
            name='productname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pdfdb',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pdfdb',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pdfdb',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
