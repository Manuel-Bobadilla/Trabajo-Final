# Generated by Django 4.2.1 on 2023-07-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_volunteer_activities'),
        ('activitie', '0002_activitiedetailpage_volunteers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitiedetailpage',
            name='volunteers',
            field=models.ManyToManyField(related_name='activities', to='users.volunteer'),
        ),
    ]
