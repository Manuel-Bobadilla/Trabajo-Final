# Generated by Django 4.2.1 on 2024-01-28 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0007_alter_activitiedetailpage_volunteering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitielistingpage',
            name='related_document',
        ),
    ]