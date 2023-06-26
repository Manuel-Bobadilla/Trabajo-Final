# Generated by Django 4.2.1 on 2023-06-02 15:38

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add a title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add a text', required=True))], classname='text_and_title'))], blank=True, null=True, use_json_field=True),
        ),
    ]