from django.db import models
from django.contrib.auth.models import User
from activitie.models import ActivitieDetailPage

# Create your models here.

class Volunteer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    activities = models.ManyToManyField(ActivitieDetailPage)
    address = models.CharField(blank=False, null=False, max_length=80, help_text="user home address")
    phone = models.IntegerField(blank=False, null=False, help_text="user phone number")

    def __str__(self):
        return str(self.user)
    
