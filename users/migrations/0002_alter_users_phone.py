# Generated by Django 4.2.1 on 2023-06-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(help_text='user phone number'),
        ),
    ]
