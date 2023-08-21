from django.shortcuts import render, get_object_or_404, redirect
from activitie.models import Volunteer, ActivitieDetailPage, User
from vehicles.models import Vehicle
import datetime

def InscriptionView(request, pk):
    user = get_object_or_404(User, id=request.user.id)
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    volunteer = get_object_or_404(Volunteer, user=user)
    if activitie.activity_start_date <= datetime.date.today() and activitie.activity_end_date > datetime.date.today():
        if activitie.volunteers.filter(id=volunteer.id).exists():
            activitie.volunteers.remove(volunteer)
            vehicle = volunteer.vehicles.filter(activitie = activitie)
            if vehicle:
                vehicle[0].activitie = None
                vehicle[0].save(force_update=True)
        else:
            activitie.volunteers.add(volunteer)

    return redirect("http://localhost:8000/activitie/") #cambiar para que determine la url de retorno de manera dinamica

def VisualizeEnrolledView(request):
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    volunteers = Volunteer.objects.filter(activities = activitie)
    vehicles = Vehicle.objects.filter(activitie = activitie)
    volunteersWithVehicle = Volunteer.objects.filter(vehicles__in=vehicles)

    return render(request,"activitie/activitie_enrolled.html",
                  {
                      "volunteers":volunteers,
                      "vehicles":vehicles,
                      "volunteersWithVehicle": volunteersWithVehicle,
                  },)


