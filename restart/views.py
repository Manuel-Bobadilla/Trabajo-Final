from django.shortcuts import render, redirect
from users.models import Volunteer, User
from restart.models import Restart
import datetime

def RestartYear(request):
    user = User.objects.get(id = request.user.id)
    restart = Restart.objects.filter(date__year = datetime.date.today().year)

    if (not user.is_superuser or restart):
        return

    restartYear = Restart(date = datetime.date.today())
    restartYear.save()

    return redirect("/boletines/")
