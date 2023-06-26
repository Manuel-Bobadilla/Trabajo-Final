from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

@register_setting
# Create your models here.
class SocialMediaSettings(BaseSiteSetting):
    whatsapp =  models.URLField(blank=True, null=True, help_text="Whatsapp URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
    email = models.URLField(blank=True, null=True, help_text="Email URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("whatsapp"),
            FieldPanel("instagram"),
            FieldPanel("email"),
        ], heading="Redes Sociales")
    ]
