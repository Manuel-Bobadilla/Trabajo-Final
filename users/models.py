from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Volunteer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(blank=False, null=False, max_length=80, help_text="user home address")
    phone = models.IntegerField(blank=False, null=False, help_text="user phone number")

    def __str__(self):
        return self.name
