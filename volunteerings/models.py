from django.db import models
from users.models import Volunteer

class Volunteering(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name="Nombre voluntariado")
    description = models.CharField(null=False, blank=False, verbose_name="Breve descripción del voluntariado")
    volunteers = models.ManyToManyField(Volunteer, related_name="volunteering", blank=True, verbose_name="Voluntarios del voluntariado")
    coordinadores = models.ManyToManyField(Volunteer, related_name="coordina", blank=True, verbose_name="Coordinadores del voluntariado")
    image = models.ImageField(help_text="Logo del voluntariado", null=True, blank=False, verbose_name="Imagen voluntariado")

    def __str__(self):
        return self.name

