from django.db import models
from users.models import Volunteer
from activitie.models import ActivitieDetailPage

class Vehicle(models.Model):
    domain = models.CharField(blank=False, null=False, max_length=10)
    brand = models.CharField(blank=False, null=False, max_length=20)
    model = models.CharField(blank=False, null=False, max_length=20)
    room = models.IntegerField(blank=False, null=True)
    proprietary = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name="vehicles")
    activitie = models.ManyToManyField(ActivitieDetailPage)

    def __str__(self):
        return self.domain
