from django.shortcuts import render, get_object_or_404, redirect
from volunteerings.models import Volunteering
from activitie.models import ActivitieDetailPage
from attendances.models import Attendance
from restart.models import Restart
from users.models import Volunteer, User
from django.db.models import Q
from django.http import QueryDict
import datetime

def Volunteerings(request):
    volunteerings = Volunteering.objects.all()
    volunteer = None

    if request.user.id:
        user = User.objects.get(id = request.user.id)
        volunteer = Volunteer.objects.get(user = user)

    return render(request, "volunteerings/volunteerings.html",{"volunteerings":volunteerings,
                                                               "volunteer": volunteer,})

def ViewVolunteering(request):
    volunteering = Volunteering.objects.get(id=request.GET.get("volunteering_id"))
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
                    "day_number": current_date.weekday(),
            })
    volunteer = None
    return render(request, "activitie/activitie_listing_page.html",{
         "posts":posts,
         "current_date":current_date,
         "volunteer":volunteer,
         "volunteering":volunteering,
    })

def ViewVolunteersVolunteeing(request):
    #verificar que quien acceda sea un coordinador
    coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & ((Q(coordinador=True) & Q(volunteering__id=request.GET.get("volunteering_id"))) | Q(user__is_superuser=True)))
    
    volunteering = Volunteering.objects.get(id=request.GET.get("volunteering_id"))
    volunteeringVolunteers = Volunteer.objects.filter(volunteering=volunteering, validated = True).order_by("user__last_name")
    restOfVolunteers = Volunteer.objects.exclude(Q(volunteering=volunteering) | Q(validated=False)).order_by("user__last_name")

    return render(request, "volunteerings/volunteers.html",{
         "volunteering":volunteering,
         "volunteeringVolunteers":volunteeringVolunteers,
         "restOfVolunteers":restOfVolunteers,
    })

def InscriptionVolunteering(request):
    #verificar que quien acceda sea un coordinador
    coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & ((Q(coordinador=True) & Q(volunteering__id=request.POST.get("volunteering_id"))) | Q(user__is_superuser=True)))
    
    volunteersInscriptedId = set()
    for attendance in request.POST:
        if attendance != "volunteering_id" and attendance != "csrfmiddlewaretoken":
            volunteersInscriptedId.add(attendance)
    volunteersInscriptedIdList = list(volunteersInscriptedId)
    volunteersInscripted = Volunteer.objects.filter(id__in = volunteersInscriptedIdList)
    volunteering = get_object_or_404(Volunteering, id=request.POST.get("volunteering_id"))
    volunteeringVolunteers = Volunteer.objects.filter(volunteering = volunteering)

    for volunteer in volunteeringVolunteers:
        if volunteer.id not in volunteersInscriptedIdList:
            activities = ActivitieDetailPage.objects.filter(volunteering = volunteering)
            for activity in activities:
                activity.volunteers.remove(volunteer)
                vehicle = volunteer.vehicles.filter(activitie = activity)
                if vehicle:
                    vehicle[0].activitie = None
                    vehicle[0].save(force_update=True)

            volunteering.volunteers.remove(volunteer)
    
    for volunteer in volunteersInscripted:
        if not volunteering.volunteers.filter(id=volunteer.id).exists():
            volunteering.volunteers.add(volunteer)

    mutable_get = request.GET.copy()
    mutable_get['volunteering_id'] = request.POST.get("volunteering_id")
    request.GET = QueryDict(mutable_get.urlencode(), mutable=False)

    return ViewVolunteersVolunteeing(request)

def AttendanceVolunteering(request):
    #verificar que quien acceda sea un coordinador
    coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & ((Q(coordinador=True) & Q(volunteering__id=request.GET.get("volunteering_id"))) | Q(user__is_superuser=True)))

    volunteering = Volunteering.objects.get(id = request.GET.get("volunteering_id"))
    volunteeringVolunteers = Volunteer.objects.filter(volunteering = volunteering)
    volunteeringActivities = ActivitieDetailPage.objects.filter(volunteering = volunteering)
    last_restart = Restart.objects.all().order_by('-date').first()

    if last_restart:
        last_restart = last_restart.date

    #agrupar por volunteer
    attendances = Attendance.objects.filter(date__gte = last_restart, volunteer__in = volunteeringVolunteers, activity__in = volunteeringActivities)

    recordsVolunteersDict = {}

    for attendance in attendances:
        if attendance.volunteer in recordsVolunteersDict:
            recordsVolunteersDict[attendance.volunteer] += 1
        else:
            recordsVolunteersDict[attendance.volunteer] = 1
    
    for volunteer in volunteeringVolunteers:
            if not volunteer in recordsVolunteersDict:
                recordsVolunteersDict[volunteer] = 0


    return render(request, "volunteerings/attendances.html",
                  {
                      "volunteers": volunteeringVolunteers,
                      "recordsVolunteersDict": recordsVolunteersDict,
                      "attendances": attendances,
                  })