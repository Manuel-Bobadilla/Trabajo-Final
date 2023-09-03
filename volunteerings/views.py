from django.shortcuts import render
from volunteerings.models import Volunteering
from activitie.models import ActivitieDetailPage
from users.models import Volunteer, User
import datetime

def Volunteerings(request):
    volunteerings = Volunteering.objects.all()

    return render(request, "volunteerings/volunteerings.html",{"volunteerings":volunteerings,})

def ViewVolunteering(request):
    posts = ActivitieDetailPage.objects.live().public()
    current_date = datetime.date.today()
    if request.user.id:
            user = User.objects.get(id=request.user.id)
            volunteer = Volunteer.objects.filter(user = user)
            if volunteer:
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
                })
    volunteer = None
    return render(request, "activitie/activitie_listing_page.html",{
         "posts":posts,
         "current_date":current_date,
         "volunteer":volunteer,
    })
