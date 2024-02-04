from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from datetime import date

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Título de la sección", label="Título")
    text = blocks.TextBlock(required=True, help_text="Texto de la sección", label="Texto")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Título y texto"

class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Campo de texto enriquecido"

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
        label = "Campo de texto simple"

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
    content = blocks.RichTextBlock(required=True, help_text="Contenido boletín", label="Contenido")
    date = blocks.DateBlock(required=True, default=date.today(), label="Fecha", help_text="Fecha del boletín")

    class Meta:
        template = "streams/bulletin.html"
        icon = "edit"
        label = "Boletines"

class CardElement(blocks.StructBlock):
    image = ImageChooserBlock(required=True, label="Imagen")
    text = blocks.RichTextBlock(required=True, help_text="Contenido", label="Texto")
    link = blocks.URLBlock(required=False, help_text="URL de la página a redireccionar en caso de desearlo, de no ser así ignorar este campo", label="Link")

    class Meta:
        template ="streams/card_element.html"
        icon = "edit"
        label = "Tarjeta"

class HorizontalAllignElements(blocks.StructBlock):
    elements = blocks.ListBlock(
        blocks.StructBlock([
            ("element", CardElement()),
        ]), label="Elementos"
    )

    class Meta:
        template ="streams/horizontal_allign_elements.html"
        icon = "edit"
        label = "Elementos Horizontales"

class Question(blocks.StructBlock):
    question = blocks.CharBlock(required=True, label="Pregunta")
    responses = blocks.ListBlock(
        blocks.StructBlock([
            ("response", blocks.CharBlock(required=True, label="Respuesta")),
        ]), label="Respuestas"
    )

    class Meta:
        template ="streams/question.html"
        icon = "edit"
        label = "Pregunta"


class FAQ(blocks.StructBlock):
    questions = blocks.ListBlock(
        Question(), label="Preguntas"
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
    voluntariado = blocks.CharBlock(required=True, help_text="Título del item de donacion, por ejemplo, nombre del voluntariado", label="Título campaña donación")
    imagen = ImageChooserBlock(required=False, help_text="Imagen de la campaña de donación, por ejemplo, imagen del voluntariado")
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
        label = "Campaña donación"

class Donaciones(blocks.StructBlock):
    elemento_donacion = blocks.ListBlock(
        DonacionVoluntariado(),
    )

    class Meta:
        template = "streams/donaciones.html"
        icon = "edit"
        label = "Donaciones"
