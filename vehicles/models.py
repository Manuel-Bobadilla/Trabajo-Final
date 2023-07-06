from django.db import models

class Vehicle(models.Model):
    domain = models.CharField(blank=False, null=False, max_length=7)

    def __str__(self):
        return self.domain
