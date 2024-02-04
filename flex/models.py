from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from streams import blocks

class FlexPage(Page):
    template = "flex/flex_page.html"

    titulo = models.CharField(max_length=100,null=True,blank=True,help_text="Título de la página")

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleTextBlock()),
            ("horizontal_allign_elements", blocks.HorizontalAllignElements()),
            ("faq", blocks.FAQ()),
            ("donaciones", blocks.Donaciones()),
        ],
        null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("titulo"),
        FieldPanel("content", heading="Contenido"),
    ]

    class Meta:
        verbose_name = "Página flexible"
        verbose_name_plural = "Páginas flexibles"

FlexPage._meta.get_field("title").help_text = "Nombre de la sección, no visto por el público. Para facilitar la organización interna de las páginas"
