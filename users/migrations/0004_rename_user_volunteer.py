# Generated by Django 4.2.1 on 2023-07-04 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_users_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Volunteer',
        ),
    ]
