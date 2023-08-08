from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

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
    date = blocks.DateBlock(required=True)

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
    itemsQuantity = blocks.IntegerBlock(required=True, help_text="cantidad de elementos")
    elements = blocks.ListBlock(
        blocks.StructBlock([
            ("element", CardElement()),
        ])
    )

    class Meta:
        template ="streams/horizontal_allign_elements.html"
        icon = "edit"
        label = "Elementos Horizontales"


