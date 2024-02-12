from django.db import models
from users.models import Volunteer

class Volunteering(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name="Nombre voluntariado")
    description = models.CharField(null=False, blank=False, verbose_name="Descripción del voluntariado")
    short_description = models.CharField(null=True, blank=True, verbose_name="Breve descripción, para vista en celulares")
    volunteers = models.ManyToManyField(Volunteer, related_name="volunteering", blank=True, verbose_name="Voluntarios del voluntariado")
    coordinadores = models.ManyToManyField(Volunteer, related_name="coordina", blank=True, verbose_name="Coordinadores del voluntariado")
    image = models.ImageField(help_text="Logo del voluntariado", null=True, blank=False, verbose_name="Imagen voluntariado")
    Whatsapp = models.CharField(help_text="Contacto de Whatsapp para el voluntariado", null=True, blank=True)
    Instagram = models.CharField(help_text="Contacto de Instagram para el voluntariado", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Voluntariado"
        verbose_name_plural = "Voluntariados"  
