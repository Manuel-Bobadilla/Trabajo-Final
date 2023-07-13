from django.shortcuts import render, get_object_or_404, redirect
from activitie.models import Volunteer, ActivitieDetailPage
from vehicles.models import Vehicle
from django.http import HttpResponseRedirect
from django.urls import reverse

def InscripcionView(request, pk):
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    volunteer = get_object_or_404(Volunteer, id=request.user.id)
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
    #print(vehicles[0].proprietary)
    #print(volunteers[0].vehicles.all())
    #todo armar diccionario clave valor con voluntarios y sus vehiculos para imprimirlos en el html

    return render(request,"activitie/activitie_enrolled.html",
                  {
                      "volunteers":volunteers,
                      "vehicles":vehicles,
                  },)


