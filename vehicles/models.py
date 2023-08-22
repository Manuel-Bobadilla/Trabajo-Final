from django.db import models
from users.models import Volunteer
from activitie.models import ActivitieDetailPage

class Vehicle(models.Model):
    domain = models.CharField(blank=False, null=False, max_length=7)
    brand = models.CharField(blank=False, null=False, max_length=20)
    model = models.CharField(blank=False, null=False, max_length=20)
    room = models.IntegerField(blank=False, null=False)
    proprietary = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name="vehicles")
    activitie = models.ForeignKey(ActivitieDetailPage, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.domain
