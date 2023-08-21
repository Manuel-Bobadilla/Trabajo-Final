from django.db import models
from django.contrib.auth.models import User


class Volunteer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(blank=False, null=False, max_length=80, help_text="volunteer's home address")
    phone = models.CharField(blank=False, null=False, max_length=20, help_text="volunteer's phone number")
    neighborhood = models.CharField(blank=False, null=False, max_length=80, help_text="volunteer's neighborhood")
    university = models.CharField(blank=False, null=False, max_length=80, help_text="volunteer's university")
    university_file = models.CharField(blank=False, null=False, max_length=20, help_text="volunteer's university file")

    def __str__(self):
        return str(self.user.first_name + " " + self.user.last_name)
    
