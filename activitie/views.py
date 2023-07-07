from django.shortcuts import render, get_object_or_404, redirect
from activitie.models import Volunteer, ActivitieDetailPage
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

