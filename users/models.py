from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Volunteer(models.Model):

    name = models.CharField(blank=False, null=False, max_length=80, help_text="first and last name")
    address = models.CharField(blank=False, null=False, max_length=80, help_text="user home address")
    phone = models.IntegerField(blank=False, null=False, help_text="user phone number")
    email = models.CharField(blank=False, null=False, max_length=100, help_text="email address")
    #password todo

    def __str__(self):
        return self.name
