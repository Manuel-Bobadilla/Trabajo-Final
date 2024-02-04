# Generated by Django 4.2.1 on 2024-02-04 20:27

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0063_remove_flexpage_subtitle_flexpage_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add a title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add a text', required=True))])), ('full_rich_text', streams.blocks.RichTextBlock()), ('simple_rich_text', streams.blocks.SimpleTextBlock()), ('horizontal_allign_elements', wagtail.blocks.StructBlock([('elements', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('element', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='imagen', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='Contenido', required=True)), ('link', wagtail.blocks.URLBlock(help_text='URL, si es necesario', required=False))]))])))])), ('faq', wagtail.blocks.StructBlock([('questions', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(help_text='Pregunta', required=True)), ('responses', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('response', wagtail.blocks.CharBlock(help_text='Respuesta', required=True))])))])))])), ('donaciones', wagtail.blocks.StructBlock([('elemento_donacion', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('voluntariado', wagtail.blocks.CharBlock(help_text='Titulo del item de donacion', required=True)), ('imagen', wagtail.images.blocks.ImageChooserBlock(help_text='imagen del voluntariado', required=False)), ('alias', wagtail.blocks.CharBlock(help_text='Alias para recibir donaciones', required=False)), ('sugeridos', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(blank='True', help_text='Elementos sugeridos para donar', required=False), blank=True, required=False)), ('contactos', wagtail.blocks.StreamBlock([('Instagram', wagtail.blocks.StructBlock([('cuenta', wagtail.blocks.CharBlock(help_text='Nombre cuenta instagram', required=True))])), ('Whatsapp', wagtail.blocks.StructBlock([('numero', wagtail.blocks.CharBlock(help_text='Número celular', required=True))]))], required=False, use_json_field=True))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]