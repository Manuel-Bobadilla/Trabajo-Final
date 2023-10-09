# Generated by Django 4.2.1 on 2023-10-09 20:25

import datetime
from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0035_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add a title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add a text', required=True))])), ('full_rich_text', streams.blocks.RichTextBlock()), ('simple_rich_text', streams.blocks.SimpleTextBlock()), ('meeting_point', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Nombre punto de encuentro', required=True)), ('text', wagtail.blocks.CharBlock(help_text='Dirección punto de encuentro', required=True))])), ('material_publication', wagtail.blocks.StructBlock([('material', wagtail.blocks.CharBlock(help_text='Material', required=True)), ('caracteristics', wagtail.blocks.StreamBlock([('caracteristica', wagtail.blocks.CharBlock(help_text='Caracteristica Material', required=True))]))])), ('raffle', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Titulo Rifa', required=True)), ('price', wagtail.blocks.CharBlock(help_text='Precio', required=True)), ('prizes', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('prize', wagtail.blocks.CharBlock(help_text='Premios', required=True))])))])), ('contacts', wagtail.blocks.StructBlock([('email', wagtail.blocks.CharBlock(help_text='Email', required=True)), ('phone', wagtail.blocks.CharBlock(help_text='Celular', required=True)), ('instagram', wagtail.blocks.CharBlock(help_text='Instagram', required=True))])), ('images', streams.blocks.ImagePost()), ('bulletins', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(help_text='Contenido', required=True)), ('date', wagtail.blocks.DateBlock(default=datetime.date(2023, 10, 9), required=True))])), ('horizontal_allign_elements', wagtail.blocks.StructBlock([('elements', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('element', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='imagen', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='Contenido', required=True)), ('link', wagtail.blocks.URLBlock(help_text='URL, si es necesario', required=False))]))])))])), ('faq', wagtail.blocks.StructBlock([('questions', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('number', wagtail.blocks.IntegerBlock(help_text='Número de pregunta, asegurese de que no se repita', required=True)), ('question', wagtail.blocks.CharBlock(help_text='Pregunta', required=True)), ('responses', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('response', wagtail.blocks.CharBlock(help_text='Respuesta', required=True))])))])))])), ('column_elements', wagtail.blocks.StructBlock([('elements', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('elements', wagtail.blocks.StreamBlock([('horizontal_allign_elements', wagtail.blocks.StructBlock([('elements', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('element', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='imagen', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='Contenido', required=True)), ('link', wagtail.blocks.URLBlock(help_text='URL, si es necesario', required=False))]))])))])), ('material_publication', wagtail.blocks.StructBlock([('material', wagtail.blocks.CharBlock(help_text='Material', required=True)), ('caracteristics', wagtail.blocks.StreamBlock([('caracteristica', wagtail.blocks.CharBlock(help_text='Caracteristica Material', required=True))]))])), ('meeting_point', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Nombre punto de encuentro', required=True)), ('text', wagtail.blocks.CharBlock(help_text='Dirección punto de encuentro', required=True))])), ('card_element', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='imagen', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='Contenido', required=True)), ('link', wagtail.blocks.URLBlock(help_text='URL, si es necesario', required=False))])), ('rich_text_box', streams.blocks.RichTextBlock())]))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
