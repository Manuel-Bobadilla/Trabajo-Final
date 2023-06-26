# Generated by Django 4.2.1 on 2023-06-26 18:46

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0009_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add a title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add a text', required=True))])), ('full_rich_text', streams.blocks.RichTextBlock()), ('simple_rich_text', streams.blocks.SimpleTextBlock()), ('meeting_point', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Nombre punto de encuentro', required=True)), ('text', wagtail.blocks.CharBlock(help_text='Dirección punto de encuentro', required=True))])), ('material_publication', wagtail.blocks.StructBlock([('material', wagtail.blocks.CharBlock(help_text='Material', required=True)), ('caracteristics', wagtail.blocks.StreamBlock([('caracteristica', wagtail.blocks.CharBlock(help_text='Caracteristica Material', required=True))]))])), ('raffle', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Titulo Rifa', required=True)), ('price', wagtail.blocks.DecimalBlock(help_text='Precio', required=True)), ('prizes', wagtail.blocks.StreamBlock([('prize', wagtail.blocks.CharBlock(help_text='Premios', required=True))]))])), ('contacts', wagtail.blocks.StructBlock([('email', wagtail.blocks.CharBlock(help_text='Email', required=True)), ('phone', wagtail.blocks.CharBlock(help_text='Celular', required=True)), ('instagram', wagtail.blocks.CharBlock(help_text='Instagram', required=True))])), ('images', streams.blocks.ImagePost()), ('bulletins', streams.blocks.Bulletin())], blank=True, null=True, use_json_field=True),
        ),
    ]
