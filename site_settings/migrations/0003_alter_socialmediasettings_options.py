# Generated by Django 4.2.1 on 2024-02-04 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_alter_socialmediasettings_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialmediasettings',
            options={'verbose_name': 'Contacto redes sociales', 'verbose_name_plural': 'Contactos redes sociales'},
        ),
    ]