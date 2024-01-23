from django.shortcuts import render, redirect
from users.models import Volunteer, User
from vehicles.models import Vehicle
from volunteerings.models import Volunteering
from activitie.models import ActivitieDetailPage
from restart.models import Restart
import datetime

def RestartYear(request):
    user = User.objects.get(id = request.user.id)
    restart = Restart.objects.filter(date__year = datetime.date.today().year)

    if (not user.is_superuser or restart):
        return

    activities = ActivitieDetailPage.objects.all()
    vehicles = Vehicle.objects.filter(activitie__in = activities)
    volunteerings = Volunteering.objects.all()

    for vehicle in vehicles:
        vehicle.activitie.clear()

    for activity in activities:
        activity.volunteers.clear()

    for volunteering in volunteerings:
        volunteering.volunteers.clear()

    restartYear = Restart(date = datetime.date.today())
    restartYear.save()

    return redirect("/boletines/")
