# Generated by Django 4.2.1 on 2024-02-04 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0009_remove_activitielistingpage_custom_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitiedetailpage',
            name='activity_end_date',
            field=models.DateField(default=datetime.date(2024, 11, 30), help_text='Fecha inicio de vigencia del post de la actividad'),
        ),
        migrations.AlterField(
            model_name='activitiedetailpage',
            name='activity_start_date',
            field=models.DateField(default=datetime.date(2024, 2, 28), help_text='Fecha inicio de vigencia del post de la actividad'),
        ),
    ]
