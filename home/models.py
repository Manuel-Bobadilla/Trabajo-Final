from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from streams import blocks

class HomePage(Page):
    template = "home/home_page.html"

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleTextBlock()),
            ("meeting_point", blocks.MeetingPoint()),
            ("material_publication", blocks.MaterialPublication()),
            ("raffle", blocks.Raffle()),
            ("contacts", blocks.Contacts()),
            ("images", blocks.ImagePost()),
            ("bulletins", blocks.Bulletin()),
            ("horizontal_allign_elements", blocks.HorizontalAllignElements()),
        ],
        null=True, blank=True, use_json_field=True)

    subtitle = models.CharField(max_length=100,null=True,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
