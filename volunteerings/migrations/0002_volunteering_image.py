# Generated by Django 4.2.1 on 2023-09-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteerings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteering',
            name='image',
            field=models.ImageField(help_text='Logo del voluntariado', null=True, upload_to=''),
        ),
    ]
