from django.db import models

from users.models import Volunteer
from activitie.models import ActivitieDetailPage

class Attendance(models.Model):
    volunteer = models.ForeignKey(Volunteer, null=False, on_delete=models.CASCADE, related_name="attendances")
    activity = models.ForeignKey(ActivitieDetailPage, null=True, on_delete=models.SET_NULL, related_name="record")
    date = models.DateField(null=False)
