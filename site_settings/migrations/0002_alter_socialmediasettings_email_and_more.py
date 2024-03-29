# Generated by Django 4.2.1 on 2024-01-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='email',
            field=models.CharField(blank=True, help_text='Dirección Email', null=True),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='instagram',
            field=models.CharField(blank=True, help_text='Nombre cuenta Instagram', null=True),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='whatsapp',
            field=models.CharField(blank=True, help_text='Número Whatsapp', null=True),
        ),
    ]
