from django.shortcuts import render
from volunteerings.models import Volunteering
from activitie.models import ActivitieDetailPage
from users.models import Volunteer, User
import datetime

def Volunteerings(request):
    volunteerings = Volunteering.objects.all()

    return render(request, "volunteerings/volunteerings.html",{"volunteerings":volunteerings,})

def ViewVolunteering(request):
    volunteering = Volunteering.objects.get(id=request.POST.get("volunteering_id"))
    posts = ActivitieDetailPage.objects.filter(volunteering=volunteering)
    current_date = datetime.date.today()
    inscripted = False
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        volunteer = Volunteer.objects.filter(user = user)
        volunteeringsOfVolunteer = Volunteering.objects.filter(volunteers__in = volunteer)
        if volunteering in volunteeringsOfVolunteer:
                inscripted = True
        if volunteer[0].validated:
            activities = ActivitieDetailPage.objects.filter(volunteers = volunteer[0])
            vehicles = volunteer[0].vehicles.all()
            vehicles = vehicles
            activities = activities
            volunteer = volunteer[0]
            return render(request, "activitie/activitie_listing_page.html",{
                    "posts":posts,
                    "current_date":current_date,
                    "vehicles":vehicles,
                    "activities":activities,
                    "volunteer":volunteer,
                    "inscripted":inscripted,
                    "volunteering":volunteering,
            })
    volunteer = None
    return render(request, "activitie/activitie_listing_page.html",{
         "posts":posts,
         "current_date":current_date,
         "volunteer":volunteer,
         "volunteering":volunteering,
    })
