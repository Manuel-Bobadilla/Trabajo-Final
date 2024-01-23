from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSiteSetting):
    whatsapp =  models.CharField(blank=True, null=True, help_text="Número Whatsapp")
    instagram = models.CharField(blank=True, null=True, help_text="Nombre cuenta Instagram")
    email = models.CharField(blank=True, null=True, help_text="Dirección Email")

    panels = [
        MultiFieldPanel([
            FieldPanel("whatsapp"),
            FieldPanel("instagram"),
            FieldPanel("email"),
        ], heading="Redes Sociales")
    ]
