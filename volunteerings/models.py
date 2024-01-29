from django.db import models
from users.models import Volunteer

class Volunteering(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(null=False, blank=False)
    volunteers = models.ManyToManyField(Volunteer, related_name="volunteering")
    coordinadores = models.ManyToManyField(Volunteer, related_name="coordina")
    image = models.ImageField(help_text="Logo del voluntariado", null=True, blank=False)

    def __str__(self):
        return self.name

