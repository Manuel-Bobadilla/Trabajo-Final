from django.shortcuts import render, get_object_or_404
from activitie.models import Volunteer, ActivitieDetailPage
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

def InscripcionView(request, pk):
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    volunteer = get_object_or_404(Volunteer, id=request.user.id)
    if activitie.volunteers.filter(id=volunteer.id).exists():
        activitie.volunteers.remove(volunteer)
    else:
        activitie.volunteers.add(volunteer)

    return redirect("http://localhost:8000/") #cambiar esto a mantenerse en la pagina

