from django.db import models
from users.models import Volunteer
from activitie.models import ActivitieDetailPage

class Attendance(models.Model):
    volunteer = models.ForeignKey(Volunteer, null=False, on_delete=models.CASCADE, related_name="attendances", verbose_name="Voluntario")
    activity = models.ForeignKey(ActivitieDetailPage, null=True, on_delete=models.SET_NULL, related_name="record", verbose_name="Actividad")
    date = models.DateField(null=False, verbose_name="Fecha")
    activity_title = models.CharField(max_length=255, blank=True, verbose_name="Título de la actividad")

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"  
