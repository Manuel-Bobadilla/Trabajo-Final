# Generated by Django 4.2.1 on 2023-08-12 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('activitie', '0003_alter_activitiedetailpage_volunteers'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitielistingpage',
            name='related_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
    ]