# Generated by Django 4.2.1 on 2023-07-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0001_initial'),
        ('users', '0007_volunteer_activities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='activities',
            field=models.ManyToManyField(to='activitie.activitiedetailpage'),
        ),
    ]