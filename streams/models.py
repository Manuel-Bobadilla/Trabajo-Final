from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from streams import blocks

# Create your models here.
class BulletinListingPage(Page):
    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text="overwrites the default title")
    
    template = "streams/bulletin_page.html"

    content = StreamField(
        [
            ("bulletins", blocks.Bulletin()),
        ],
        null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
            FieldPanel("custom_title"),
            FieldPanel("content")
        ]
    
class BulletinDetailPage(Page):
    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text="overwrites the default title")

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
        ],
        null=True, blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("content"),
    ]