from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from datetime import date

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add a title")
    text = blocks.TextBlock(required=True, help_text="Add a text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Rich Text"

class SimpleTextBlock(blocks.RichTextBlock):

    def __init__(
        self,
        required=True,
        help_text=None,
        editor="default",
        features=None,
        max_length=None,
        validators=(),
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]
        

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Simple Text"

class MeetingPoint(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Nombre punto de encuentro")
    text = blocks.CharBlock(required=True, help_text="Dirección punto de encuentro")

    class Meta:
        template = "streams/meeting_point.html"
        icon = "edit"
        label = "Punto de Encuentro"


class MaterialPublication(blocks.StructBlock):
    material = blocks.CharBlock(required=True, help_text="Material")
    caracteristics = blocks.StreamBlock([
        ("caracteristica", blocks.CharBlock(required=True, help_text="Caracteristica Material")),
    ])

    class Meta:
        template = "streams/material_publication.html"
        icon = "edit"
        label = "Elemento Donación"

class Raffle(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Titulo Rifa")
    price = blocks.CharBlock(required=True, help_text="Precio")
    prizes = blocks.ListBlock(
        blocks.StructBlock([
            ("prize", blocks.CharBlock(required=True, help_text="Premios")),
        ])
    )

    class Meta:
        template = "streams/raffle.html"
        icon = "edit"
        label = "Rifa"

class Contacts(blocks.StructBlock):
    email = blocks.CharBlock(required=True, help_text="Email")
    phone = blocks.CharBlock(required=True, help_text="Celular")
    instagram = blocks.CharBlock(required=True, help_text="Instagram")

    class Meta:
        template = "streams/contacts.html"
        icon = "edit"
        label = "Contactos"

class ImagePost(ImageChooserBlock):

    class Meta:
        template = "streams/image.html"
        icon = "edit"
        label = "Imagen"

class Bulletin(blocks.StructBlock):
    content = blocks.RichTextBlock(required=True, help_text="Contenido")
    date = blocks.DateBlock(required=True, default=date.today())

    class Meta:
        template = "streams/bulletin.html"
        icon = "edit"
        label = "Boletin"

class CardElement(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text="imagen")
    text = blocks.RichTextBlock(required=True, help_text="Contenido")
    link = blocks.URLBlock(required=False, help_text="URL, si es necesario")

    class Meta:
        template ="streams/card_element.html"
        icon = "edit"
        label = "Tarjeta"

class HorizontalAllignElements(blocks.StructBlock):
    elements = blocks.ListBlock(
        blocks.StructBlock([
            ("element", CardElement()),
        ])
    )

    class Meta:
        template ="streams/horizontal_allign_elements.html"
        icon = "edit"
        label = "Elementos Horizontales"

class Question(blocks.StructBlock):
    number = blocks.IntegerBlock(required=True, help_text="Número de pregunta, asegurese de que no se repita")
    question = blocks.CharBlock(required=True, help_text="Pregunta")
    responses = blocks.ListBlock(
        blocks.StructBlock([
            ("response", blocks.CharBlock(required=True, help_text="Respuesta")),
        ])
    )

    class Meta:
        template ="streams/question.html"
        icon = "edit"
        label = "Pregunta"


class FAQ(blocks.StructBlock):
    questions = blocks.ListBlock(
        Question()
    )

    class Meta:
        template = "streams/faq.html"
        icon = "edit"
        label = "Preguntas Frecuentes"

class Column(blocks.StructBlock):
    elements = blocks.StreamBlock([
        ("horizontal_allign_elements",HorizontalAllignElements()),
        ("material_publication", MaterialPublication()),
        ("meeting_point",MeetingPoint()),
        ("card_element", CardElement()),
        ("rich_text_box", RichTextBlock()),
    ])

    class Meta:
        template = "streams/column.html"
        icon = "edit"
        label = "Columna"

class ColumnElements(blocks.StructBlock):
    elements = blocks.ListBlock(
        Column()
    )

    class Meta:
        template = "streams/column_elements.html"
        icon = "edit"
        label = "Columnas"

class Instagram(blocks.StructBlock):
    cuenta = blocks.CharBlock(required=True, help_text="Nombre cuenta instagram")

    class Meta:
        template = "streams/instagram.html"
        icon = "edit"
        label = "Instagram"

class Whatsapp(blocks.StructBlock):
    numero = blocks.CharBlock(required=True, help_text="Número celular")

    class Meta:
        template = "streams/whatsapp.html"
        icon = "edit"
        label = "Whatsapp"

class DonacionVoluntariado(blocks.StructBlock):
    voluntariado = blocks.CharBlock(required=True, help_text="Titulo del item de donacion")
    imagen = ImageChooserBlock(required=False, help_text="imagen del voluntariado")
    alias = blocks.CharBlock(required=False, help_text="Alias para recibir donaciones")
    
    sugeridos = blocks.ListBlock(
        blocks.CharBlock(required=False, blank="True", help_text="Elementos sugeridos para donar"), required=False, blank=True
    )   

    contactos = blocks.StreamBlock([
        ("Instagram", Instagram()),
        ("Whatsapp", Whatsapp()),
    ], required=False, use_json_field=True)

    class Meta:
        template = "streams/donaciones_voluntariado.html"
        icon = "edit"
        label = "Donaciones"

class Donaciones(blocks.StructBlock):
    elemento_donacion = blocks.ListBlock(
        DonacionVoluntariado(),
    )

    class Meta:
        template = "streams/donaciones.html"
        icon = "edit"
        label = "Donacion"
