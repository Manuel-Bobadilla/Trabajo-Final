from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField

class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1

    banner = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name = "+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = "+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
        PageChooserPanel("banner_cta")
    ]

    class Meta:
        verbose_name = "HOME PAGE"
        verbose_name_plural = "HOME PAGES"