# Generated by Django 4.2.1 on 2023-08-21 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activitie', '0005_activitiedetailpage_activity_end_date_and_more'),
        ('users', '0010_alter_volunteer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='record', to='activitie.activitiedetailpage')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='users.volunteer')),
            ],
        ),
    ]