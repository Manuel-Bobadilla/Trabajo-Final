# Generated by Django 4.2.1 on 2024-02-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_volunteer_address_alter_volunteer_birthdate_and_more'),
        ('volunteerings', '0004_alter_volunteering_coordinadores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteering',
            name='coordinadores',
            field=models.ManyToManyField(blank=True, related_name='coordina', to='users.volunteer', verbose_name='Coordinadores del voluntariado'),
        ),
        migrations.AlterField(
            model_name='volunteering',
            name='description',
            field=models.CharField(verbose_name='Breve descripción del voluntariado'),
        ),
        migrations.AlterField(
            model_name='volunteering',
            name='image',
            field=models.ImageField(help_text='Logo del voluntariado', null=True, upload_to='', verbose_name='Imagen voluntariado'),
        ),
        migrations.AlterField(
            model_name='volunteering',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre voluntariado'),
        ),
        migrations.AlterField(
            model_name='volunteering',
            name='volunteers',
            field=models.ManyToManyField(blank=True, related_name='volunteering', to='users.volunteer', verbose_name='Voluntarios del voluntariado'),
        ),
    ]
