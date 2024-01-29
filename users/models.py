from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
import datetime


class Volunteer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(blank=False, null=False, max_length=80, help_text="Direccon")
    phone = models.CharField(blank=False, null=False, max_length=20, help_text="Telefono")
    neighborhood = models.CharField(blank=False, null=False, max_length=80, help_text="Barrio")
    university = models.CharField(blank=False, null=False, max_length=80, help_text="Universidad")
    university_file = models.CharField(blank=False, null=False, max_length=20, help_text="Legajo universidad")
    career = models.CharField(blank=True, null=True, max_length=30, help_text="Carrera")
    birthdate = models.DateField(blank=False, null=True, help_text="Fecha de nacimiento")
    dni = models.CharField(blank=False, null=False, max_length=20, help_text="DNI")
    ingreso = models.DateField(blank=False, null=False, default = datetime.date.today, help_text="Fecha de ingreso al VUCC")
    coordinador = models.BooleanField(blank=False, null=False, default=False, help_text="Coordinador de voluntariado")
    validated = models.BooleanField(blank=False, null=False, help_text="Voluntario validado")

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
                        vehicle[0].activitie = None
                        vehicle[0].save(force_update=True)
        
        if not self.coordinador:
            Volunteering = apps.get_model('volunteerings', 'Volunteering')

            volunteeringCoordinator = Volunteering.objects.filter(coordinadores = self)

            for volunteering in volunteeringCoordinator:
                volunteering.coordinadores.remove(self)


        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user.last_name + " " + self.user.first_name)
    
