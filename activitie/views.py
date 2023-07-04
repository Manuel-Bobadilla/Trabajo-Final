from django.shortcuts import render, get_object_or_404
from .models import ActivitieDetailPage
from users.models import Volunteer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

def InscripcionView(request, pk):
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    user = get_object_or_404(Volunteer, id=request.user.id)
    user.activities.add(activitie)

    return redirect("http://localhost:8000/") #cambiar esto a mantenerse en la pagina

