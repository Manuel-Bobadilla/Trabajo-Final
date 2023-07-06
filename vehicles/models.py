from django.db import models
from users.models import Volunteer

class Vehicle(models.Model):
    domain = models.CharField(blank=False, null=False, max_length=7)
    brand = models.CharField(blank=False, null=False, max_length=20)
    model = models.CharField(blank=False, null=False, max_length=20)
    proprietary = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

    def __str__(self):
        return self.domain
