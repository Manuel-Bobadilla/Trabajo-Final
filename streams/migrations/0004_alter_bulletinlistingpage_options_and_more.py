# Generated by Django 4.2.1 on 2024-02-04 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0003_delete_bulletindetailpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bulletinlistingpage',
            options={'verbose_name': 'Página boletines', 'verbose_name_plural': 'Páginas boletines'},
        ),
        migrations.RemoveField(
            model_name='bulletinlistingpage',
            name='custom_title',
        ),
    ]
