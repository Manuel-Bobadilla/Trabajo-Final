# Generated by Django 4.2.1 on 2024-02-07 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0003_alter_attendance_activity_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name': 'Asistencia', 'verbose_name_plural': 'Asistencias'},
        ),
    ]
