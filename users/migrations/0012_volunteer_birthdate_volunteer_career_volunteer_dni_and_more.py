# Generated by Django 4.2.1 on 2023-08-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_volunteer_neighborhood_volunteer_university_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='birthdate',
            field=models.DateField(help_text='Fecha de nacimiento', null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='career',
            field=models.CharField(blank=True, help_text='Carrera', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='dni',
            field=models.CharField(default='123', help_text='DNI', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='address',
            field=models.CharField(help_text='Direccon', max_length=80),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='neighborhood',
            field=models.CharField(help_text='Barrio', max_length=80),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(help_text='Telefono', max_length=20),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='university',
            field=models.CharField(help_text='Universidad', max_length=80),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='university_file',
            field=models.CharField(help_text='Legajo universidad', max_length=20),
        ),
    ]
