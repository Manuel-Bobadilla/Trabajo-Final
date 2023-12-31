# Generated by Django 4.2.1 on 2023-06-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='first and last name', max_length=80)),
                ('address', models.CharField(help_text='user home address', max_length=80)),
                ('phone', models.IntegerField(help_text='user phone number', max_length=10)),
                ('email', models.CharField(help_text='email address', max_length=100)),
            ],
        ),
    ]
