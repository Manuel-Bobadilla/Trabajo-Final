from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
import datetime


class Volunteer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name="Usuario vinculado")
    address = models.CharField(blank=False, null=False, max_length=80, verbose_name="Dirección")
    phone = models.CharField(blank=False, null=False, max_length=20, verbose_name="Teléfono")
    neighborhood = models.CharField(blank=False, null=False, max_length=80, verbose_name="Barrio")
    birthdate = models.DateField(blank=False, null=False, default=datetime.date.today, verbose_name="Fecha de nacimiento")
    dni = models.CharField(blank=False, null=False, max_length=20, verbose_name="DNI")
    ingreso = models.DateField(blank=False, null=False, default = datetime.date.today, verbose_name="Fecha de ingreso al VUCC")
    university = models.CharField(blank=True, null=True, max_length=80, verbose_name="Universidad")
    university_file = models.CharField(blank=True, null=True, max_length=20, verbose_name="Legajo universitario")
    career = models.CharField(blank=True, null=True, max_length=30, verbose_name="Carrera")
    coordinador = models.BooleanField(blank=False, null=False, default=False, verbose_name="Coordinador del VUCC")
    validated = models.BooleanField(blank=False, null=False, default=False, help_text="Voluntario validado", verbose_name="Validado")

    def save(self, *args, **kwargs):
        if not self.validated:
            if self.id:
                Volunteering = apps.get_model('volunteerings', 'Volunteering')
                ActivitieDetailPage = apps.get_model('activitie', 'ActivitieDetailPage')

                volunteerings = Volunteering.objects.filter(volunteers = self)
                activities = ActivitieDetailPage.objects.filter(volunteers = self)
                volunteeringCoordinator = Volunteering.objects.filter(coordinadores = self)

                for volunteering in volunteerings:
                    volunteering.volunteers.remove(self)

                for volunteering in volunteeringCoordinator:
                    volunteering.coordinadores.remove(self)

                for activity in activities:
                    activity.volunteers.remove(self)
                    vehicle = self.vehicles.filter(activitie = activity)
                    if vehicle:
                        vehicle[0].activitie.remove(activity)
                        vehicle[0].save(force_update=True)
                        if vehicle[0].domain == "Pasajero":
                            vehicle[0].delete()
        
        if not self.coordinador:
            Volunteering = apps.get_model('volunteerings', 'Volunteering')

            volunteeringCoordinator = Volunteering.objects.filter(coordinadores = self)

            for volunteering in volunteeringCoordinator:
                volunteering.coordinadores.remove(self)


        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user.last_name + " " + self.user.first_name)

    class Meta:
        verbose_name = "Voluntario"
        verbose_name_plural = "Voluntarios"  
    
